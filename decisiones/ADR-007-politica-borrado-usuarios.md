# ADR-007: Política de borrado de usuarios

**Estado:** Aceptado
**Fecha:** 2026-09-24

## Contexto

El backoffice de usuarios (#8) no permitía eliminar usuarios: la única salida era
desactivarlos (`is_active=false`), y las filas se acumulaban. Al probar el flujo de
invitación (#60) quedaron usuarios de prueba imposibles de limpiar. El ticket #70 agrega
`DELETE /admin/users/{id}` admin-only.

La tabla `log_events` registra acciones con `user_id` (FK NOT NULL) — hoy los imports de
Guaraní. La pregunta: ¿qué pasa con los eventos de un usuario que se elimina?

## Decisión

**Bloquear el borrado si el usuario tiene `log_events` asociados** (409 con mensaje
explícito). La FK existente ya lo impide a nivel DB; el service traduce el `IntegrityError`
sin query previa.

`log_events` es un log de auditoría: `user_id` es la atribución de quién ejecutó la acción.
Nullificarlo degradaría la trazabilidad sin necesidad real — los usuarios de prueba que
motivaron el ticket no tienen eventos.

Además, un admin no puede eliminarse a sí mismo (422), mismo criterio que el self-lockout
de la edición de roles (`_ensure_no_self_lockout` en `UserService`).

## Alternativas consideradas

- **`user_id` nullable + `ON DELETE SET NULL`**: permite borrar siempre, pero pierde la
  atribución del evento — inaceptable en un log de auditoría. Descartada.
- **Pre-check explícito con query a `log_events`** (vía `LogEventService` inyectado): mismo
  resultado con más plumbing y una query extra; la FK es la fuente de verdad. Descartada.

## Consecuencias

- Un usuario con imports registrados no puede eliminarse (sí desactivarse). Si el bloqueo
  molesta en el futuro, revisar la política (ej. anonimizar en lugar de borrar).
- El frontend muestra el `detail` del 409/422 tal cual; no necesita conocer la política.
- Cobertura: unit tests del service + integración del endpoint (401/403/404/204/422/409).
