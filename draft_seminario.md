# Draft — Seminario Final: Proyecto Finisterre — Académika

> Estado: borrador inicial — sujeto a revisión

---

## 1. Motivación

Las carreras de informática de la Universidad Nacional de Quilmes (UNQ) —Licenciatura en Informática (LI) y Tecnicatura Universitaria en Programación Informática (TPI)— generan un volumen significativo de datos académicos a través del sistema SIU Guaraní y otras fuentes complementarias. Sin embargo, la capacidad de los directores de carrera y docentes para extraer conclusiones accionables de esos datos es limitada: los reportes son estáticos, los formatos son heterogéneos, y el análisis manual es costoso en tiempo.

En 2021, Ignacio Yegro desarrolló como Seminario Final un sistema de seguimiento académico para la LI-UNQ que nunca llegó a producción. Si bien ese trabajo estableció un marco conceptual y un dominio valioso, el avance de la inteligencia artificial —en particular los modelos de lenguaje y las técnicas de RAG (Retrieval-Augmented Generation)— abre la posibilidad de un approach radicalmente más potente y usable.

Este Seminario propone construir una plataforma web AI-first para el seguimiento académico de carreras de informática en la UNQ.

---

## 2. Objetivo general

Diseñar, desarrollar y validar una plataforma web que permita a directores de carrera y docentes de la UNQ analizar, consultar y comprender la situación académica de estudiantes, materias y carreras mediante una interfaz conversacional basada en IA, con datos provenientes del SIU Guaraní y fuentes complementarias.

---

## 3. Objetivos específicos

1. **Análisis de trayectorias estudiantiles:** identificar estudiantes al ritmo del plan de estudios, estudiantes que avanzan más rápido, y estudiantes "trabados" (definición formal pendiente).
2. **Análisis de materias críticas:** detectar qué materias concentran mayor cantidad de estudiantes trabados, reprobados o con bajo avance.
3. **Análisis de deserción:** identificar patrones y puntos de quiebre en la trayectoria donde ocurre la deserción.
4. **Proyección de inscripciones:** estimar la demanda de materias en próximos cuatrimestres para mejorar la planificación docente.
5. **Análisis de equipos docentes:** identificar fortalezas y necesidades de los equipos docentes en función de la demanda proyectada y el rendimiento de sus materias.
6. **Estandarización de datos:** definir un pipeline de ingesta que normalice los diferentes formatos de reportes del SIU Guaraní y otras fuentes.
7. **Interfaz conversacional:** proveer un chatbot como interfaz principal de consulta, con contexto configurable por el usuario (al estilo NotebookLM).
8. **Privacidad y seguridad:** garantizar que los datos sensibles de los estudiantes no sean expuestos en ninguna capa del sistema.

---

## 4. Descripción de la solución propuesta

### 4.1 Inspiración conceptual

La plataforma toma como referencia el modelo de **NotebookLM** (Google): un sistema donde el usuario gestiona un conjunto de *fuentes de información* (sources), un chatbot con RAG puede responder preguntas sobre ese contexto acotado, y el sistema puede generar reportes o contenido derivado.

Adaptado al contexto académico universitario, esto se traduce en:

- **Sources:** reportes del SIU Guaraní (historial académico, inscripciones, etc.), planes de estudio, datos complementarios aportados por directores y docentes.
- **Chatbot:** interfaz conversacional que responde preguntas sobre la situación de la carrera, materias y estudiantes, con acceso controlado y auditable al contexto.
- **Generación de contenido:** producción de reportes, resúmenes y visualizaciones a demanda.

### 4.2 Componentes principales

| Componente | Descripción |
|---|---|
| **Ingesta y normalización** | Pipeline para procesar reportes en distintos formatos (CSV, Excel, PDF) desde SIU Guaraní y otras fuentes |
| **Base de conocimiento** | Almacenamiento estructurado + embeddings para búsqueda semántica (RAG) |
| **Motor analítico** | Cálculo de métricas académicas: trayectorias, trabas, proyecciones, deserción |
| **API backend** | Endpoints REST/GraphQL para frontend y chatbot |
| **Chatbot (LLM + RAG)** | Interfaz conversacional con contexto acotado a los datos cargados |
| **Frontend web** | Dashboard + interfaz de chat + gestión de sources |
| **Capa de seguridad** | Control de acceso por rol, anonimización de datos sensibles, audit log |

### 4.3 Usuarios y roles

- **Director de carrera** (rol principal): acceso completo a todos los datos y funcionalidades.
- **Docente:** acceso acotado a las materias que dicta.
- *(Potencial)* **Administrador del sistema:** gestión de usuarios y fuentes de datos.

---

## 5. Alcance inicial

El sistema se construirá y validará para las dos carreras de informática de la UNQ:

- Licenciatura en Informática (LI)
- Tecnicatura Universitaria en Programación Informática (TPI)

Los datos del proyecto de Nacho (Yegro, 2021) serán usados como referencia para el modelo de dominio y como datos de prueba donde sea aplicable.

---

## 6. Definiciones pendientes

- **"Trabar" en una materia:** definición formal de cuándo se considera que un estudiante está "trabado" (¿N intentos? ¿tiempo sin inscribirse? ¿combinación?). Acordar con Eugenio y Denise.
- Fuentes de datos disponibles y formatos reales (gestión con Eugenio y la universidad).
- Modelo de privacidad: qué datos se pueden usar en el contexto del LLM y cuáles deben quedar anonimizados o fuera.
- Stack tecnológico definitivo.

---

## 7. Relación con el trabajo de Yegro (2021)

El trabajo de Nacho estableció el dominio del problema (modelos de Alumno, Carrera, Materia, Plan de Estudio) y un conjunto de métricas académicas relevantes. Este Seminario reconoce ese antecedente y toma de él:

- El **modelo de dominio** como punto de partida.
- Los **datos de prueba** como base para validación.
- Las **métricas analíticas** desarrolladas como insumo para el motor analítico.

La diferencia fundamental es el paradigma: de un dashboard estático a una plataforma conversacional AI-first.

---

## 8. Próximos pasos

- [ ] Refinar definiciones pendientes con directores de carrera (Eugenio, Denise) y directora del seminario (Gabriela)
- [ ] Evaluar stack tecnológico (LLM provider, vector store, framework web)
- [ ] Definir modelo de privacidad y política de manejo de datos sensibles
- [ ] Diseñar arquitectura de alto nivel
- [ ] Relevar formatos reales de datos del SIU Guaraní disponibles

---

*Autor: Leandro Di Lorenzo — Seminario Final, Lic. en Informática, UNQ*  
*Directora: Dra. Gabriela Arévalo*  
*Draft inicial: abril 2026*
