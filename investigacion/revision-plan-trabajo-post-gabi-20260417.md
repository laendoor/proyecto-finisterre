# Revisión del Plan de Trabajo — post reunión Gabi 16/04

Relevamiento de lo que hay que actualizar antes de mandárselo a Mara.
Tres categorías: **A — resolver ahora** (tenemos el dato), **B — requiere trabajo** (hay que escribir/investigar), **C — pendiente externo** (necesitamos algo de afuera).

---

## Sección 1 — Introducción

### [A] Cambiar duración a 6 meses

- Línea: `duración estimada de **20 semanas (~5 meses)**`
- Cambiar a 6 meses (requisito reglamentario formal — lo dijo Gabi explícitamente).
- Está en §7 Cronograma, no en §1, pero lo mapeo acá para no perderlo.

### [A] Completar motivo por el que Nacho nunca llegó a producción

- Línea: `pero el sistema nunca llegó a producción [DRAFT: Lean — completar con el motivo concreto]`
- Gabi lo explicó en la reunión: **falta de tiempo para mantenimiento**. Sin mantenimiento constante, el stack tecnológico quedó desactualizado. No estaba previsto quién lo mantendría.
- Texto propuesto: "...pero el sistema no llegó a ponerse en producción por falta de mantenimiento sostenido, así el stack tecnológico quedó desactualizado."

### [B] Datos de otras carreras para contraponer (el `[ver si tenemos datos...]`)

- Línea: `8.600 estudiantes activos al cierre de 2024 [Arévalo, 2025] contra [ver si tenemos datos de otras carreras para contraponer]`
- Fuente disponible: CSV de datos abiertos UNQ → `https://transparencia.unq.edu.ar/wp-content/uploads/2025/08/Estudiantes-Datos-abiertos-a-082025.csv`
- Hay que bajar el CSV, identificar las columnas relevantes (inscriptos/reinscriptos por carrera), y armar la comparativa.
- Gabi sugirió también mencionarlo en la intro como ejemplo de **información disponible pero fragmentada** (está hasta 2022 solamente en el portal público).
- Agregar referencia a la **Ley de Acceso a la Información Pública** como marco legal para el uso de datos abiertos.

### [B] Reescribir la oración sobre la brecha ingresantes/egresados

- Línea: `...lo que genera una brecha creciente cuya gestión requiere capacidades analíticas que hoy no están disponibles en ninguna herramienta. [Hay que mejorar esta oración, queda medio rara con respecto a la anterior]`
- Hay que hacer fluir mejor la transición: primero se dice que las carreras son las más numerosas (matrículas), después que los egresos no crecen al mismo ritmo, y de ahí que se necesitan herramientas analíticas. La oración actual mezcla causa y consecuencia de forma confusa.

---

## Sección 2 — Motivación

### [C] Ejemplos concretos de decisiones operativas

- Línea: `[DRAFT: agregar más ejemplos concretos con Eugenio y Denise]`
- Pendiente de la reunión con Eugenio y Denise (tentativo 23/04). Ellos van a poder dar ejemplos reales de qué necesitan en cada momento del ciclo académico.

### [B] Análisis del gap ingresantes/egresados

- Línea: `[DRAFT: incorporar análisis del gap ingresantes/egresados — pendiente de obtener datos de egresos]`
- La columna de egresos debería estar en el CSV de transparencia UNQ. Verificar y completar.

---

## Sección 3 — Estado del arte

### [B] Completar "Trabajos previos en la UNQ"

- Gabi dijo que en el trabajo de Nacho hay referencias a desarrollos similares en otras instituciones. Revisar el informe de Yegro.

### [B] TODO: Desarrollos similares en otras instituciones

- Revisar informe de Yegro (Gabi confirmó que él tiene esta sección).
- Revisar informe de Rinaudo (el otro trabajo que usó Lean).

### [B] TODO: Aplicaciones AI-first para análisis de datos

- NotebookLM, plataformas de BI conversacional, etc.
- Justificar el enfoque Text-to-SQL/RAG sobre dashboards tradicionales.

---

## Sección 6 — Metodología (fases 3, 4 y 5 — el feedback más importante de Gabi)

El problema según Gabi: el plan habla de qué tecnología implementa cada fase, pero no deja claro **qué valor concreto entrega al usuario** en cada una. Alguien que no sea de sistemas (biotecnólogos, ingenieros en la comisión evaluadora) lee "interfaz conversacional basada en Text-to-SQL" y no entiende qué puede hacer con eso.

**Lo que hay que hacer:** para cada fase 3/4/5, agregar explícitamente:

- Qué puede hacer el usuario como resultado de esta fase
- Ejemplos concretos de consultas o reportes que ahora son posibles

### [B] Fase 2 — agregar ejemplo de reportes predefinidos

- Actual: "Motor analítico-determinístico: métricas de trayectorias, materias críticas, deserción, proyección de inscripciones / Panel Analítico: visualización e interfaz para disparar análisis predefinidos"
- Agregar: un par de ejemplos concretos de reportes ("¿cuál es la materia con mayor tasa de abandono?", "histograma de inscriptos LI 2015-2025"). Esto hace tangible lo de "predefinidos".

### [B] Fase 3 — resultado concreto para el usuario

- Actual: "Interfaz conversacional Hari: primera versión funcional basada en Text-to-SQL / El asistente genera consultas SQL desde lenguaje natural contra la base de datos académica"
- Agregar: qué tipo de consultas puede hacer el usuario en lenguaje natural que antes no podía. Ej: "A partir de esta fase, el director puede pedirle a Hari 'mostrame los estudiantes que cursaron Análisis 1 más de dos veces y no aprobaron' y el sistema genera la consulta correspondiente."
- Aclarar: además de análisis predefinidos, Hari permite **análisis custom on the fly**.

### [B] Fase 4 — resultado concreto para el usuario

- Actual: "Incorporación de RAG con embeddings (pgvector) como segundo enfoque de Hari / Mejoras al pipeline Text-to-SQL a partir de los aprendizajes de Fase 3"
- Agregar: qué cambia para el usuario vs Fase 3. ¿Qué tipo de preguntas responde mejor RAG que Text-to-SQL? Ejemplo: consultas que cruzan datos cuantitativos con información cualitativa (normativa, planes de estudio como texto).

### [B] Fase 5 — aclarar que hay evaluación con usuarios reales

- Actual: "Evaluación comparativa de ambos enfoques (Text-to-SQL vs RAG) sobre un conjunto de consultas canónicas"
- Agregar: que las consultas canónicas vienen de los relevamientos con Eugenio y Denise — no son arbitrarias. Y que la validación es con los usuarios reales de la herramienta.

### [B] Stack tecnológico — justificación por tecnología

- Actual: una sola línea con lista de tecnologías + link al ADR
- Gabi pidió explícitamente que en el plan de trabajo se justifique brevemente cada tecnología. El ADR-003 tiene el detalle, pero el plan necesita un párrafo o tabla con el "por qué" de cada una.
- Para la comisión: Python (ecosistema estadístico, pandas, etc.), FastAPI (liviano y async), Next.js/React (mejor soporte de ecosistema frontend), PostgreSQL (estándar de facto + pgvector), Claude API (swappable, mejor soporte para code), Docker (reproducibilidad).

---

## Sección 7 — Cronograma

### [A] Cambiar duración a 6 meses

- Línea: `duración estimada de **20 semanas (~5 meses)**`
- Cambiar a: `duración estimada de **6 meses**`
- Gabi: reglamentariamente son 6 meses mínimo.

---

## Sección 9 — Licencia

### [C] Definir licencia

- `[TODO: definir licencia específica — MIT o Apache 2.0]`
- Decidir y poner.

---

## Sección 10 — Referencias

### [C] Confirmar tipo de publicación del trabajo de Gabi

- `[DRAFT: confirmar tipo de publicación con Gabi]`
- Pendiente — preguntarle a Gabi.

### [B] Completar bibliografía

- `[TODO: agregar bibliografía de soporte — RAG, LLM, análisis estadístico académico, AI-first UX]`
- Pendiente de investigación.

---

## Orden de ataque sugerido

1. **[A] ahora:** duración 6 meses (§7), motivo Nacho no llegó a producción (§1)
2. **[B] próximo:** reescribir oración brecha §1, detallar fases 3/4/5 con ejemplos concretos (§6), agregar justificación del stack (§6)
3. **[B] después de reunión con Eugenio/Denise:** ejemplos concretos de decisiones operativas (§2), consultas canónicas para §6 fases 3/4/5
4. **[B] investigación pendiente:** estado del arte (§3), gap ingresantes/egresados con CSV (§2), datos de otras carreras (§1)
5. **[C] externos:** licencia (§9), tipo publicación Gabi (§10), bibliografía (§10)
