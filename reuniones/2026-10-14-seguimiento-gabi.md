# Reunión: Seguimiento con Gabi — demo backoffice, importación CSV y priorización de reportes

**Fecha:** 2026-10-14
**Participantes:** Leandro Di Lorenzo, Gabriela Arevalo
**Contexto:** Reunión semanal de seguimiento. Demo del backoffice de Académika (accesos e importación CSV) y definición del orden de trabajo del workspace analítico: reportes predefinidos primero, métricas custom con IA después.

## Feedback recibido

- (Gabi) Va a explorar la aplicación y registrar en un documento las sugerencias, faltantes o cambios necesarios en la visualización de datos, para que Lean genere las incidencias correspondientes.
- (Gabi + Lean) Los reportes de métricas predefinidas van antes que la generación de métricas personalizadas con IA.
- (Gabi) Desacuerdo pedagógico con el uso de `LEFT JOIN` y valores nulos en la enseñanza (complican la programación con controles de nulidad); cuestiona enseñar SQL en lugar de centrarse en álgebra relacional pura.
- (Lean) Los nulos representan ausencia válida de valor según el contexto; los `LEFT JOIN` son herramienta estándar y SQL es indispensable para cruce, ordenamiento y manipulación práctica — debate docente, sin impacto en decisiones del proyecto.
- (Lean) La carga de planillas Guaraní exige estructura estricta ligada al modelo de datos para evitar inconsistencias (distinto de archivos solo para procesamiento por IA).

## Decisiones

- **Gabi revisa la app y documenta feedback**: explora la herramienta y registra modificaciones y funciones deseadas en un documento.
- **Lean genera issues desde ese documento** una vez que Gabi lo complete.
- **Reportes predefinidos antes que IA custom**: implementar primero las métricas predefinidas (base: trabajo de Nacho Yegro); la generación de métricas personalizadas con IA (consultas dinámicas) viene después.

## Accionables

- [ ] **Gabi**: explorar la aplicación y documentar sugerencias, faltantes o cambios en la visualización de datos.
- [ ] **Lean**: crear los issues en base al documento de feedback de Gabi.
- [ ] **Lean**: implementar los reportes de métricas predefinidas (base: trabajo de Nacho Yegro).

## Próximos pasos

- Enfocar la siguiente fase en el workspace analítico: métricas predefinidas sobre trayectorias estudiantiles, deserción y materias críticas (el backoffice actual queda como base de datos crudos importados).
- Tras los reportes predefinidos, implementar métricas personalizadas con IA mediante consultas dinámicas.

## Preguntas abiertas

- No se registraron preguntas abiertas nuevas en esta reunión.
