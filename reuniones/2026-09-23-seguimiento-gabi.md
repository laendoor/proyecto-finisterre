# Reunión: Seguimiento con Gabi — realineamiento, invitaciones y estrategia de datos

**Fecha:** 2026-09-23
**Participantes:** Leandro Di Lorenzo, Gabriela Arevalo
**Contexto:** Reunión semanal de seguimiento (la primera desde el 2026-06-04). Realineamiento general: demo del panel de administración de Académika, estado del sistema de invitaciones, y discusión sobre la estrategia de datos (sintéticos vs. reales) de cara a la presentación.

## Feedback recibido

- (Gabi) Hoy la app sube datos sintéticos y está bien, pero antes de la presentación hay que resolver cómo se cargan los datos reales — no puede seguir defendiendo ante los docentes que usen las herramientas de la UNQ (sistemas inestables).
- (Gabi) Sobre la restricción de dominio en invitaciones: si se quiere restringir no pasa nada, pero le parece que no hace falta.
- (Gabi) Sobre pseudonimización: ella trabajaría con el legajo tapado, pero eso aplicaba cuando el sistema iba a estar en servidores de la UNQ. Si se hostea afuera (que es lo obvio), necesita poder buscar la información. No es bloqueante por ahora: "después vemos".
- (Gabi) Panel de admin: "está hermoso".
- (Gabi) Sobre el ritmo lento (Lean viene a full con el trabajo): "vamos de a poco, vamos que podés".
- (Lean) Disclaimer propio: la comisión de seminarios finales plantea que no hay que gastar plata en el seminario final; está gastando igual (droplet ~USD 5-7/mes + suscripción al asistente) porque es inviable hacer una aplicación decente sin eso.

## Decisiones

- **Restricción de dominio de invitaciones**: sacarla o hacerla configurable por el admin (que defina dominios aceptables).
- **Estrategia de datos**: los datos reales viven reales en la base (recuperables por super-permisos vía mapeo); los roles del día a día trabajan con referencias (legajo pseudonimizado). La forma de búsqueda/consulta para Gabi se define más adelante, cuando se resuelva el hosting.
- **La seguridad no depende de dónde se hostee** (UNQ vs. afuera) sino de las capas de control de acceso.
- **Próxima reunión**: miércoles 2026-09-30 a las 18:00 (puede demorar hasta las 18:15).

## Formalidades / requisitos académicos

- La comisión de seminarios finales desaconseja gastar dinero en el seminario final; el deploy de Académika hoy corre a cargo de Lean (droplet + suscripción).
- Antes de la presentación hay que definir el esquema de carga de datos reales (Gabi lo levanta como requisito explícito).

## Accionables

- [ ] **Lean**: terminar el sistema de invitaciones (70-80% listo) e invitar a Gabi
- [ ] **Lean**: quitar o hacer configurable la restricción de dominio UNQ en invitaciones
- [ ] **Lean**: corregir el panel de admin — "planes de estudio" duplicado e inconsistencias de números entre filas
- [ ] **Lean**: mostrar los datasets restantes (carreras, planes de estudio, correlativas, inscripciones, historial de cursadas) con una vista clásica con filtros, para que el que sube los datos pueda verificar lo importado
- [ ] **Lean**: avanzar en las 15 tareas técnicas planificadas, priorizando motor analítico y métricas (pseudonimización reversible, flujo de importación, trayectorias estudiantiles, regla de deserción, tasas agregadas, materias críticas, proyección de inscripciones, visualización)
- [ ] **Gabi**: al recibir la invitación, usar la app y devolver feedback (vistas útiles, fixes, confusiones)

## Próximos pasos

- Cerrar el backoffice de datos crudos y arrancar el motor analítico, para poder tener discusiones más productivas con Gabi (hoy solo hay para mostrar carga de datos)
- Pasar Académika a Eugenio y Denise cuando tenga madurez suficiente, para que definan antes del lanzamiento
- Definir estrategia de datos reales y hosting antes de la presentación

## Preguntas abiertas

- ¿Cómo se cargan los datos reales para la presentación, dado que la UNQ no ofrece infraestructura confiable?
- ¿Hosting final: externo pago (en contra de la recomendación de la comisión) o infraestructura UNQ?
- Si se hostea afuera, ¿cómo busca Gabi la información sobre datos pseudonimizados? (mapeo legajo ↔ identidad)
- ¿Por qué aparece "planes de estudio" duplicado y con números inconsistentes en el panel? (técnico, a revisar)
