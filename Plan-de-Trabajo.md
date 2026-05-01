# Plan de Trabajo

## Proyecto Finisterre: Académika como plataforma web AI-first para seguimiento académico

**Alumno:** Leandro Di Lorenzo Etchepare\
**Directora:** Dra. Gabriela Arévalo\
**Carrera:** Licenciatura en Informática\
**Departamento:** Ciencia y Tecnología — Universidad Nacional de Quilmes\
**Fecha:** abril 2026\
**Estado:** En construcción

---

## 1. Introducción

Las instituciones educativas generan volúmenes crecientes de datos académicos (inscripciones, cursadas, aprobaciones, trayectorias) que en la práctica son difíciles de aprovechar. Los sistemas de gestión académica existentes, como el SIU Guaraní[^siu-guarani] o [id], permiten el registro y acceso a los datos pero pocas herramientas de análisis. Quienes toman decisiones sobre carreras y materias deben generarse sus herramientas de análisis ad-hoc con información muchas veces fragmentada o difícil de consultar en tiempo real.

Esta problemática no es ajena a las carreras de informática del Departamento de Ciencia y Tecnología de la Universidad Nacional de Quilmes (DCyT-UNQ). Las carreras Licenciatura en Informática (LI) y Tecnicatura Universitaria en Programación Informática (TPI)  concentran la matrícula más numerosa de la Universidad. Según el Portal de Transparencia de la UNQ[^transparencia], en 2024 la TPI registró 4.517 estudiantes (inscriptos + reinscriptos) y la LI 3.272, sumando 7.789 entre ambas. Esto es más del triple que la carrera de Contador Público, la tercera carrera más numerosa de la institución:

| Carrera                          | Alumnos 2024 |
| -------------------------------- | -----------: |
| **TPI**                          |    **4.517** |
| **LI**                           |    **3.272** |
| Contador Público                 |        2.493 |
| Lic. en Educación (CCC)          |        2.290 |
| Lic. en Comercio Internacional   |        1.801 |

El crecimiento ha sido sostenido y acelerado: en 2016 ambas carreras sumaban 1.121 estudiantes; en 2024, 7.789 — casi siete veces más en ocho años. Sin embargo, los egresos no crecen al mismo ritmo: en 2024 las dos carreras sumaron 55 egresados contra 3.040 nuevos inscriptos. La brecha entre quienes ingresan y quienes egresan es estructural y se amplía año a año, lo que convierte la gestión de trayectorias estudiantiles en un problema urgente que las herramientas disponibles hoy no permiten un análisis eficaz.

En 2021, Juan Ignacio Yegro desarrolló como Seminario Final un prototipo avanzado de aplicación de seguimiento académico para estas carreras[^Yegro-2021]. Ese trabajo estableció un modelo de dominio sólido y un conjunto de métricas académicas relevantes, pero el sistema no llegó a ponerse en producción por falta de mantenimiento sostenido: sin recursos dedicados a su operación, el stack tecnológico quedó desactualizado antes de poder ser adoptado. El avance en inteligencia artificial —en particular los modelos de lenguaje grandes (LLMs) y las técnicas de Retrieval-Augmented Generation (RAG)— abre hoy la posibilidad de retomar ese trabajo, extenderlo y construir sobre sus cimientos una plataforma más potente y usable.

Este plan de trabajo propone el diseño, desarrollo y validación de **Académika**: una plataforma web AI-first para el seguimiento académico de las carreras de informática de la UNQ, orientada a la dirección de carreras y al equipo docente.

---

## 2. Motivación

Las direcciones de carrera de la UNQ operan bajo tres tipos de momentos de decisión con características y necesidades de información distintas:

1. **Decisiones operativas** — en general relacionadas al período de inscripciones (previas y posteriores): requieren información rápida y precisa sobre demanda y cupos, disponibilidad del equipo docente y asignación de recursos. [DRAFT: agregar más ejemplos concretos con Eugenio y Denise]
2. **Decisiones de mediano plazo** — durante el armado de la oferta académica: requieren proyecciones y estimados de demanda por materia para el cuatrimestre siguiente.
3. **Decisiones estratégicas** — durante el resto del cuatrimestre: permiten análisis más profundos sobre trayectorias estudiantiles, deserción, rendimiento y planificación de largo plazo.

La herramienta actual (SIU Guaraní) provee datos crudos pero no análisis. No existe una plataforma que permita a las direcciones de carrera explorar sus datos en lenguaje natural, detectar estudiantes en riesgo o anticipar situaciones críticas antes de que escalen.

El volumen del problema justifica la inversión. Con 7.789 estudiantes en 2024 [^transparencia], LI y TPI son las carreras más grandes de la UNQ. Y la tasa de egreso es estructuralmente baja: en los últimos años la relación entre nuevos inscriptos y egresados no superó el 2%:

| Año  | Nuevos inscriptos | Egresados |
| ---- | ----------------: | --------: |
| 2019 |               910 |        22 |
| 2021 |               703 |        20 |
| 2022 |             1.281 |        28 |
| 2023 |             3.341 |        47 |
| 2024 |             3.040 |        55 |

La demanda de ingreso se multiplicó por más de tres entre 2022 y 2024 — en buena parte impulsada por el auge de la inteligencia artificial —, pero los egresos crecen a un ritmo que no guarda proporción.

---

## 3. Estado del arte

### Trabajos previos en la UNQ

El antecedente directo más relevante es el trabajo de Yegro (2021), que desarrolló una aplicación de seguimiento académico para las carreras de informática de la UNQ con foco en métricas de trayectoria estudiantil y gestión de inscripciones. El presente trabajo toma de él el modelo de dominio (Alumno, Carrera, Materia, Plan de Estudios) y las métricas analíticas como punto de partida, y extiende el enfoque hacia una interfaz conversacional basada en IA.

### Desarrollos similares en otras instituciones

[TODO: investigar y documentar — sistemas de seguimiento académico en otras universidades, plataformas de analytics académico]

### Aplicaciones de IA conversacional en contextos de análisis de datos

[TODO: documentar el estado del arte en herramientas AI-first para análisis de datos (NotebookLM, plataformas de BI conversacional), justificar el enfoque RAG sobre dashboards tradicionales]

---

## 4. Objetivo general

Diseñar, desarrollar y validar una plataforma web que permita a la dirección de carreras y al equipo docente de la UNQ analizar, consultar y comprender la situación académica de estudiantes, materias y carreras mediante una interfaz conversacional basada en inteligencia artificial, con datos provenientes del SIU Guaraní y fuentes complementarias, orientada a la toma de decisiones en los distintos momentos del ciclo académico.

---

## 5. Objetivos específicos

1. Relevar los requerimientos funcionales y no funcionales de las direcciones de carrera de LI y TPI.
2. Diseñar el modelo de dominio y la arquitectura del sistema, incluyendo el modelo de privacidad y ofuscación de datos sensibles.
3. Desarrollar el pipeline de ingesta, ofuscación y normalización de datos provenientes del SIU Guaraní y fuentes complementarias.
4. Desarrollar el motor analítico-determinístico con métricas académicas predefinidas (trayectorias estudiantiles, materias críticas, deserción, proyección de inscripciones).
5. Desarrollar la interfaz conversacional basada en IA integrada con los datos académicos, evaluando y comparando dos enfoques: generación de consultas SQL desde lenguaje natural (Text-to-SQL) y recuperación semántica por similitud (RAG con embeddings).
6. Desarrollar el frontend web con Panel Analítico e interfaz de chat.
7. Realizar pruebas unitarias y de integración del sistema.
8. Poner en producción dentro del entorno de la UNQ.
9. Documentar el sistema y redactar el informe final.

---

## 6. Metodología

El desarrollo se realizará con metodología iterativa e incremental. Cada fase produce un incremento funcional del sistema que puede ser evaluado y validado antes de avanzar a la siguiente.

El trabajo se organiza en un **Preludio** de investigación y diseño, seguido de cinco fases de desarrollo y un cierre, denominados con los títulos de la *Serie Fundación* de Isaac Asimov [^asimov-fundacion]:

**Preludio** — *Preludio a la Fundación*

- Relevamiento de requerimientos con las direcciones de carrera
- Relevamiento de datos disponibles en SIU Guaraní y otras fuentes utilizadas
- Diseño del modelo de dominio y arquitectura del sistema
- Diseño del modelo de privacidad y ofuscación
- Entrega del plan de trabajo

**Fase 1** — *Fundación*

- Estructura del repositorio y configuración del entorno de desarrollo
- App base: autenticación, roles (direcciones de carrera, equipo docente), estructura de base de datos
- Deploy temprano en Digital Ocean (CI/CD, contenedores)

**Fase 2** — *Fundación e Imperio*

- Pipeline de ingesta, ofuscación y normalización de datos del SIU Guaraní
- Motor analítico-determinístico: métricas de trayectorias, materias críticas, deserción, proyección de inscripciones
- Panel Analítico: visualización e interfaz para disparar análisis predefinidos

Al finalizar esta fase, el director de carrera puede acceder a reportes estructurados sobre la situación académica de la carrera: cuáles son las materias con mayor tasa de abandono, cuántos estudiantes llevan más de tres años sin aprobar una materia, o qué proyección de inscriptos se espera para el próximo cuatrimestre basada en la tendencia histórica. Estos análisis — que antes requerían exportar datos de Guaraní y procesarlos manualmente en planillas — se generan con un clic desde la plataforma.

**Fase 3** — *Segunda Fundación*

- Interfaz conversacional Hari: primera versión funcional basada en Text-to-SQL
- El asistente genera consultas SQL desde lenguaje natural contra la base de datos académica
- Gestión de fuentes (sources) y permisos por rol

A partir de esta fase, el director puede realizarle a Hari consultas arbitrarias en lenguaje natural sobre los datos académicos — análisis que los reportes predefinidos de Fase 2 no contemplan. Por ejemplo: *"mostrame los estudiantes que cursaron Análisis Matemático más de dos veces y todavía no aprobaron"*, o *"¿cuántos alumnos de TPI aprobaron todas las materias del primer año pero no se reinscribieron?"*. El sistema traduce esas preguntas a consultas SQL y devuelve los resultados directamente, sin que el usuario necesite conocer el modelo de datos ni escribir código.

**Fase 4** — *Los límites de la Fundación*

- Incorporación de RAG con embeddings (pgvector) como segundo enfoque de Hari
- Mejoras al pipeline Text-to-SQL a partir de los aprendizajes de Fase 3

Text-to-SQL opera bien sobre datos tabulares cuantitativos, pero hay preguntas que requieren cruzar esos datos con documentos cualitativos — planes de estudio, reglamentos, normativa de correlatividades. En esta fase Hari incorpora un segundo enfoque basado en recuperación semántica (RAG): el sistema indexa esos documentos y puede responder consultas como *"¿qué dice el reglamento de correlatividades sobre Redes 1 y cuántos alumnos están actualmente bloqueados por esa correlativa?"* o *"¿los cambios introducidos en el plan de estudios 2019 afectaron la tasa de egreso de los ingresantes de ese año?"*. El usuario interactúa con la misma interfaz de chat; la diferencia es el tipo de información que Hari puede cruzar.

**Fase 5** — *Fundación y Tierra*

- Evaluación comparativa de ambos enfoques (Text-to-SQL vs RAG) sobre un conjunto de consultas canónicas relevadas con los directores de carrera
- Selección del enfoque definitivo o diseño híbrido según resultados
- Validación del sistema completo con Eugenio Cálcena y Denise Pari como usuarios reales

Las consultas canónicas de evaluación no son arbitrarias: se construyen a partir del relevamiento con los directores de carrera realizado en la etapa de Preludio, y representan las preguntas reales que surgen en el trabajo cotidiano de gestión. La evaluación combina métricas objetivas (exactitud de las respuestas, latencia) con validación cualitativa por parte de los propios usuarios. El resultado de esta fase determina la configuración definitiva del asistente — ya sea un enfoque único o una arquitectura híbrida que combine ambos según el tipo de consulta.

**Cierre**

- Validación del sistema con las direcciones de carrera; iteración final
- Pruebas finales y estabilización
- Documentación técnica y de usuario
- Redacción y entrega del informe final
- Defensa de trabajo

**Stack tecnológico principal:** la selección de tecnologías está guiada por tres criterios: madurez del ecosistema para el dominio estadístico-analítico, compatibilidad con los requerimientos de privacidad y ofuscación de datos, y posibilidad de reemplazar el modelo de lenguaje sin modificar el resto del sistema (ver [ADR-002](decisiones/ADR-002-model-swappability.md) y [ADR-003](decisiones/ADR-003-stack-academika.md)).

| Tecnología | Rol | Justificación |
|---|---|---|
| Python | Backend y análisis de datos | Ecosistema estadístico maduro (pandas, NumPy); estándar de facto en ciencia de datos y procesamiento de lenguaje natural |
| FastAPI | API REST | Liviano, asíncrono nativo, genera documentación OpenAPI automáticamente; adecuado para APIs analíticas con alta concurrencia |
| Next.js + React | Frontend web | SSR nativo, ecosistema de componentes amplio, soporte para interfaces reactivas e interactivas |
| PostgreSQL + pgvector | Base de datos | Estándar de facto para datos relacionales; pgvector permite búsqueda semántica en la misma base sin infraestructura adicional |
| LlamaIndex | Orquestación RAG | Abstrae los detalles de indexado, embedding y recuperación; facilita comparar estrategias de retrieval sin reescribir la capa de integración |
| Claude API | Modelo de lenguaje | Sólido razonamiento sobre código y SQL; arquitectura swappable — reemplazar el modelo es decisión de configuración, no de refactoring |
| Docker + GitHub Actions | Infraestructura y CI/CD | Reproducibilidad del entorno entre desarrollo y producción; validación automática en cada cambio |

**Privacidad:** Los datos sensibles de los estudiantes no son expuestos en ninguna capa del sistema. Durante el desarrollo, los datos de prueba son ofuscados localmente por las direcciones de carrera mediante herramientas provistas por el proyecto antes de ser enviados. La plataforma final incorpora una capa de ofuscación y anonimización en el pipeline de ingesta.

[id]: http://example.com/  "Optional Title Here"
[^siu-guarani]: <https://documentacion.siu.edu.ar/wiki/SIU-Guarani>
[^transparencia]: Portal de Transparencia de la UNQ — Datos abiertos de estudiantes (actualizado a agosto 2025). <https://transparencia.unq.edu.ar/?page_id=53>. Datos disponibles en acceso abierto conforme a la Ley N° 27.275 de Derecho de Acceso a la Información Pública.
[^asimov-fundacion]: Asimov, Isaac. *Serie Fundación*. <https://es.wikipedia.org/wiki/Serie_Fundaci%C3%B3n>

---

## 7. Cronograma

El proyecto inicia en **abril de 2026** y tiene una duración estimada de **6 meses** [^2]. La escritura del informe corre en paralelo con el desarrollo desde la aprobación del plan de trabajo.

- **S1-S3 — abril 2026**
  - Preludio — *Preludio a la Fundación*
- **S3-S7 — abril-mayo 2026**
  - Fase 1 — *Fundación*
- **S6-S10 — mayo-junio 2026**
  - Fase 2 — *Fundación e Imperio*
- **S10-S13 — julio 2026**
  - Fase 3 — *Segunda Fundación*
- **S12-S15 — julio-agosto 2026**
  - Fase 4 — *Los límites de la Fundación*
- **S15-S17 — agosto 2026**
  - Fase 5 — *Fundación y Tierra*
- **S16-S20 — agosto-septiembre 2026**
  - Cierre

[^2]: Las semanas se solapan entre fases de forma deliberada — el inicio de cada fase no requiere que la anterior esté completamente cerrada.

---

## 8. Lugar de trabajo

El trabajo será desarrollado de forma remota y en las instalaciones de la Universidad Nacional de Quilmes. Se mantendrán reuniones semanales con la directora del Seminario. El sistema se desplegará inicialmente en un servidor propio (Digital Ocean) como prueba de concepto y luego se migrará a la infraestructura de la UNQ.

---

## 9. Licencia

El código será licenciado bajo una licencia libre avalada por la OSI (Open Source Initiative). El código fuente será subido a un repositorio de acceso público.

[TODO: definir licencia específica — MIT o Apache 2.0]

---

## 10. Referencias bibliográficas

- Yegro, Juan Ignacio (2021). *Aplicación de Gestión Académica para gestionar decisiones en Dirección de Carreras de Informática.* Seminario Final, Licenciatura en Informática, UNQ.

[TODO: agregar bibliografía de soporte — RAG, LLM, análisis estadístico académico, AI-first UX]
