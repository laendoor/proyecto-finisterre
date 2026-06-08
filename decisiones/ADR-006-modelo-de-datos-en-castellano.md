# ADR-006: Modelo de datos en castellano

**Estado:** Aceptado
**Fecha:** 2026-06-08

## Contexto

El modelo de datos inicial de Académika usaba terminología en inglés (Student, Course, Degree, StudyPlan, CourseEnrollment, CoursePrerequisite). En reuniones con la directora del seminario (2026-06-04) la terminología inglesa generó confusiones concretas al hablar del modelo: los usuarios target son directores de carrera que operan en español y cuya referencia es el sistema Guaraní, también en español. La distancia entre el vocabulario del dominio y el del código aumentaba la fricción en cada discusión de diseño.

## Decisión

Renombrar todas las entidades del modelo de dominio a castellano. Mapeo principal:

- `Student` → `Alumno`
- `Course` → `Materia`
- `Degree` → `Carrera`
- `StudyPlan` → `PlanDeEstudio`
- `CourseEnrollment` → `Cursada`
- `CoursePrerequisite` → `Correlativa`
- LKPs: `lkp_academic_status` → `lkp_estado_academico`, etc.
- Columnas: `first_name` → `nombre`, `doc_id` → `dni`, `year` → `anio`, etc.

**Frontera explícita:** los tipos intermedios de parsing del importador Guaraní (`types.py`) se mantienen en inglés — son estructuras internas de transformación, no modelos de dominio.

**Regla resultante:** tablas, modelos ORM, schemas Pydantic y rutas REST en español; tipos internos de parsing en inglés.

## Consecuencias

- El código refleja el vocabulario con el que trabajan los usuarios, reduciendo fricción en discusiones de diseño y en el trabajo con la directora.
- Las rutas de la API (`/alumnos`, `/materias`, `/cursadas`) son directamente legibles para usuarios técnicos del dominio educativo.
- Se establece una frontera clara entre capa de dominio (castellano) y capa de parsing/transformación (inglés), lo que es coherente con el patrón provider → transformer del pipeline de importación.
- El código se aleja de las convenciones habituales de la industria (inglés); un desarrollador externo sin contexto puede encontrar la mezcla desconcertante.
- La migración inicial fue regenerada desde cero, descartando el historial de migraciones previas — decisión aceptable en etapa temprana del proyecto.
