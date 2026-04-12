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

Las instituciones educativas generan volúmenes crecientes de datos académicos — inscripciones, cursadas, aprobaciones, trayectorias — que en la práctica son difíciles de aprovechar. Los sistemas de gestión académica existentes, como el SIU Guaraní ampliamente utilizado en las universidades públicas argentinas, proveen acceso a los datos pero no herramientas de análisis. El resultado es que quienes toman decisiones sobre carreras y materias deben hacerlo con información fragmentada, desactualizada o difícil de consultar en tiempo real.

Esta problemática también sucede en las carreras de informática del Departamento de Ciencia y Tecnología de la Universidad Nacional de Quilmes (DCyT-UNQ) — Licenciatura en Informática (LI) y Tecnicatura Universitaria en Programación Informática (TPI) —, que además cuentan con la matrícula estudiantil más numerosa de la Universidad: 8.600 estudiantes activos al cierre de 2024 [Arévalo, 2025] contra [ver si tenemos datos de otras carreras para contraponer]. A pesar del volumen de la matrícula y del crecimiento sostenido año a año, los egresos no crecen al mismo ritmo, lo que genera una brecha creciente cuya gestión requiere capacidades analíticas que hoy no están disponibles en ninguna herramienta.[Hay que mejorar esta oración, queda medio rara con respecto a la anterior]

En 2021, Juan Ignacio Yegro desarrolló como Seminario Final un prototipo avanzado de aplicación de seguimiento académico para estas carreras [Yegro, 2021]. Ese trabajo estableció un modelo de dominio sólido y un conjunto de métricas académicas relevantes, pero el sistema nunca llegó a producción [DRAFT: Lean — completar con el motivo concreto]. El avance en inteligencia artificial —en particular los modelos de lenguaje grandes (LLMs) y las técnicas de Retrieval-Augmented Generation (RAG)— abre hoy la posibilidad de retomar ese trabajo, extenderlo y construir sobre sus cimientos una plataforma más potente y usable.

Este plan de trabajo propone el diseño, desarrollo y validación de **Académika**: una plataforma web AI-first para el seguimiento académico de las carreras de informática de la UNQ, orientada a la dirección de carreras y al equipo docente.

---

## 2. Motivación

Las direcciones de carrera de la UNQ operan bajo tres tipos de momentos de decisión con características y necesidades de información distintas:

1. **Decisiones operativas** — en general relacionadas al período de inscripciones (previas y posteriores): requieren información rápida y precisa sobre demanda y cupos, disponibilidad del equipo docente y asignación de recursos. [DRAFT: agregar más ejemplos concretos con Eugenio y Denise]
2. **Decisiones de mediano plazo** — durante el armado de la oferta académica: requieren proyecciones y estimados de demanda por materia para el cuatrimestre siguiente.
3. **Decisiones estratégicas** — durante el resto del cuatrimestre: permiten análisis más profundos sobre trayectorias estudiantiles, deserción, rendimiento y planificación de largo plazo.

La herramienta actual (SIU Guaraní) provee datos crudos pero no análisis. No existe una plataforma que permita a las direcciones de carrera explorar sus datos en lenguaje natural, detectar estudiantes en riesgo o anticipar situaciones críticas antes de que escalen.

El volumen del problema justifica la inversión: al cierre del año académico 2024, la LI contaba con aproximadamente 3.560 estudiantes activos y la TPI con 5.067, sumando más de 8.600 estudiantes en ambas carreras [Arévalo, 2025]. [DRAFT: incorporar análisis del gap ingresantes/egresados — pendiente de obtener datos de egresos]

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

El trabajo se organiza en un **Preludio** de investigación y diseño, seguido de cinco fases de desarrollo y un cierre, denominados con los títulos de la *Serie Fundación* de Isaac Asimov [^1]:

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

**Fase 3** — *Segunda Fundación*

- Interfaz conversacional Hari: primera versión funcional basada en Text-to-SQL
- El asistente genera consultas SQL desde lenguaje natural contra la base de datos académica
- Gestión de fuentes (sources) y permisos por rol

**Fase 4** — *Los límites de la Fundación*

- Incorporación de RAG con embeddings (pgvector) como segundo enfoque de Hari
- Mejoras al pipeline Text-to-SQL a partir de los aprendizajes de Fase 3

**Fase 5** — *Fundación y Tierra*

- Evaluación comparativa de ambos enfoques (Text-to-SQL vs RAG) sobre un conjunto de consultas canónicas
- Selección del enfoque definitivo o diseño híbrido según resultados

**Cierre**

- Validación del sistema con las direcciones de carrera; iteración final
- Pruebas finales y estabilización
- Documentación técnica y de usuario
- Redacción y entrega del informe final
- Defensa de trabajo

**Stack tecnológico principal:** Python + FastAPI (backend), Next.js + React (frontend), PostgreSQL + pgvector (base de datos + vectores), LlamaIndex + Claude API (RAG + LLM), Docker, GitHub Actions. Ver [ADR-003](TODO: link al repo) para detalle completo.

**Privacidad:** Los datos sensibles de los estudiantes no son expuestos en ninguna capa del sistema. Durante el desarrollo, los datos de prueba son ofuscados localmente por las direcciones de carrera mediante herramientas provistas por el proyecto antes de ser enviados. La plataforma final incorpora una capa de ofuscación y anonimización en el pipeline de ingesta.

[^1]: Asimov, Isaac. *Serie Fundación*. <https://es.wikipedia.org/wiki/Serie_Fundaci%C3%B3n>

---

## 7. Cronograma

El proyecto inicia en **abril de 2026** y tiene una duración estimada de **20 semanas (~5 meses)** [^2]. La escritura del informe corre en paralelo con el desarrollo desde la aprobación del plan de trabajo.

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
- Arévalo, Gabriela (2025). *Articulación de mecanismos de soportes universitarios para mejorar los números de egresados de las carreras de informática del DCyT-UNQ.* [DRAFT: confirmar tipo de publicación con Gabi]

[TODO: agregar bibliografía de soporte — RAG, LLM, análisis estadístico académico, AI-first UX]
