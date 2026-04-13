# ADR-004: Criterios de anonimización en anon_guarani.py

**Estado:** Aceptado
**Fecha:** 2026-04-13

## Contexto

`anon_guarani.py` es el script que prepara planillas del SIU Guaraní para uso en
desarrollo, eliminando datos personales antes de que los archivos circulen fuera
del sistema institucional. La pregunta clave fue: ¿qué columnas constituyen un
riesgo real de privacidad y cuáles no?

Una versión anterior anonimizaba también las fechas (inscripciones, cursadas,
exámenes) mediante un corrimiento de años por alumno. Se evaluó si esto era
necesario y si aportaba valor al análisis.

## Decisión

Se anonomizan **únicamente** los identificadores directos de persona:

- `legajo` — hash numérico determinístico
- `DNI` — hash numérico determinístico
- `nombre` — nombre falso determinístico (Faker, locale argentina)
- `apellido` — apellido falso determinístico (Faker, locale argentina)

Las **fechas no se modifican**. Son datos institucionales dictados por el
calendario académico (períodos de inscripción, fechas de parciales, turnos de
examen) y no identifican a un individuo por sí solas. Anonimizarlas destruiría
la capacidad de analizar cohortes, trayectorias y estacionalidad.

El script es completamente automático (sin interacción del usuario) y soporta
múltiples archivos en un solo invocation.

## Consecuencias

- La detección de columnas sensibles es automática y case-insensitive; si
  aparecen planillas con headers nuevos, se actualiza `_SENSITIVE` en el script.
- Los análisis de cohorte y trayectoria académica funcionan sin degradación.
- Se elimina la dependencia de `InquirerPy` — el script es usable en entornos
  no interactivos (scripts, CI).
- Scope acotado deliberadamente: si los directores solicitan anonimizar campos
  adicionales (email, domicilio), se extiende en ese momento.
