# Reunión: Revisión del plan de trabajo y datos abiertos UNQ

**Fecha:** 2026-04-16
**Participantes:** Leandro Di Lorenzo (Lean), Dra. Gabriela Arévalo (Gabi, directora)
**Contexto:** Gabi revisó el plan de trabajo armado por Lean. Se discutieron los datos abiertos de la UNQ como fuente para el informe, el diseño de anonimización en la app, y se coordinó la próxima reunión con los directores de carrera.

---

## Feedback recibido

**Sobre el plan de trabajo:**

- El cronograma con las fases nombradas según la serie Fundación le gustó mucho a Gabi ("muy bueno").
- Las **fases 3, 4 y 5** necesitan más detalle: el lector (especialmente los que no son de sistemas, como biotecnólogos e ingenieros en la comisión) necesita entender qué resultados concretos va a generar la app, no solo la cuestión técnica. Separar la parte tecnológica de la parte del dominio: "pipeline de ingesta" → "métricas de trayectoria académica".
- En el plan, aclarar que hay **análisis custom** (no solo predefinidos) — esto diferencia la propuesta de un simple BI.
- Agregar una sección **"Metodología de desarrollo"** en el informe (no en el plan) que explique cómo se trabajó: ADRs, bitácoras, uso de IA como asistente.
- **Stack tecnológico:** justificar por qué cada tecnología (Python sobre Java: ecosistema estadístico; PostgreSQL: la más utilizada + pgvector; etc.).
- **Duración estimada:** poner 6 meses aunque se termine antes — es requisito reglamentario formal.

**Sobre los datos de transparencia UNQ:**

- Gabi compartió dos links con datos públicos de la UNQ útiles para el informe.
- Úsalos para: (a) justificar que la información académica disponible está fragmentada y desactualizada; (b) demostrar con datos que las carreras de informática son las más numerosas de la UNQ.
- Citar la **Ley de Acceso a la Información Pública** como marco legal para el uso de datos abiertos.

**Sobre anonimización en la app (debate largo):**

- Gabi prefiere que la app muestre datos anonimizados para el análisis estadístico, para mantener objetividad (sesgo de reconocimiento de alumnos).
- El script de ofuscación de Lean es para que Eugenio/Denise lo corran y le manden planillas anonimizadas — eso está bien, pero es distinto al diseño interno de la app.
- Para la app: el patrón correcto es **tabla de mapeo** (DNI real → hash determinístico). Todas las demás tablas usan el hash. Los datos reales solo se recuperan cuando se necesita identificar a un alumno puntual.
- Para estadísticas no se necesitan nombres; para reportes individuales sí → ahí es cuando se va a buscar.
- Las **materias no se anonimizan**.

**Por qué nunca llegó el proyecto de Nacho a producción:**

- Falta de tiempo para mantenimiento. Sin mantenimiento constante, el stack tecnológico queda desactualizado y se rompe. No estaba previsto quién lo mantendría.

---

## Decisiones

- **Duración formal del plan de trabajo: 6 meses** (formalidad reglamentaria; si se termina antes, ok).
- **Patrón de anonimización en la app:** tabla de mapeo DNI → hash determinístico; el resto de las tablas usan el hash. Legajo NO se usa como pivot (post-pandemia, legajo = DNI en UNQ, inconsistente).
- **DNI como clave de mapeo** (más confiable que legajo).
- Fases 3/4/5 del plan de trabajo necesitan una pasada de mejora antes de enviárselo a la comisión.
- Gabi le pasa el plan de trabajo a **Mara** (miembro de la comisión evaluadora) para revisión previa.
- Reunión con Eugenio y Denise: Lean manda la encuesta antes, y la reunión sería el **miércoles 23/04** (de no prosperar, buscar otro día).

---

## Formalidades / requisitos académicos

- El plan de trabajo debe indicar duración de **6 meses** (reglamento del Seminario Final).
- Gabi lo envía a Mara para revisión antes de presentación formal a la comisión.

---

## Recursos compartidos

- [Portal de transparencia UNQ — datos por carrera](https://transparencia.unq.edu.ar/?page_id=53)
- [Portal de transparencia UNQ — segundo link estudiantes](https://transparencia.unq.edu.ar/?page_id=679)
- CSV con datos de ingresos/estudiantes/egresos por carrera: `https://transparencia.unq.edu.ar/wp-content/uploads/2025/08/Estudiantes-Datos-abiertos-a-082025.csv` — útil para demostrar que las carreras de informática son las más numerosas.
- Encuesta para Eugenio y Denise: ya en el Drive compartido con Gabi.

---

## Accionables

- [ ] **Lean:** mejorar fases 3, 4 y 5 del plan de trabajo con detalle de resultados concretos (separando lo técnico de lo del dominio)
- [ ] **Lean:** agregar justificación de cada tecnología del stack tecnológico en el plan de trabajo
- [ ] **Lean:** incorporar datos de transparencia UNQ en el informe (fragmentación de datos + carreras más numerosas); citar Ley de Acceso a la Información Pública
- [ ] **Gabi:** pasarle el plan de trabajo a Mara para revisión previa
- [ ] **Gabi:** contactar a Eugenio y Denise, mandarles la encuesta y proponer reunión miércoles 23/04

---

## Próximos pasos

- Presentar el plan de trabajo a la comisión una vez que Mara lo revise.
- Reunión con Eugenio y Denise (miércoles 23/04 tentativo) para validar encuesta y alinear sobre qué datos/reportes necesitan.
- Seguir con Fase 1 de Académika (tickets #3 en adelante) en paralelo.
- En el informe: sección "Metodología de desarrollo" que explique ADRs, bitácoras y uso de IA como asistente productivo.

---

## Preguntas abiertas

- Confirmación de Eugenio y Denise para el miércoles 23/04.
- Feedback de Mara sobre el plan de trabajo.
- Plazo exacto de entrega a la Comisión de Investigación (Gabi lo confirma).
