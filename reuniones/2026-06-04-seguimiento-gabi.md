# Reunión: Seguimiento Seminario — Modelo de datos y cierre del pico de inscriptos

**Fecha:** 2026-06-04
**Participantes:** Leandro Di Lorenzo, Gabriela Arevalo
**Contexto:** Reunión semanal de seguimiento. Se revisó el estado general de ambas fases, se resolvió la duda sobre el pico de inscriptos 2023-2025 con confirmación de coordinación académica, y se hizo una revisión en vivo del modelo de datos de Académika.

## Feedback recibido

- (Gabi) `credits` no debería estar en `course_enrollment` — tiene que estar en `course` (materia). Lo detectaron revisando el schema en SQL.
- (Gabi) `degrees` como nombre de tabla está bien — la confusión inicial era porque Gabi pensaba que estaba viendo una clase Python y no SQL. Convención de tabla en plural es correcta.
- (Gabi) Sobre granularidad de materias vs. planes: del 2015 al 2019 son las mismas materias (mismo código); del 2010 al 2015 no (distinto código y nombre). La clave de materias por plan debería ser `plan_id` + año del plan.
- (Gabi) Los prerrequisitos de los datos de Nacho son una mezcla de Guaraní + planillas propias de la carrera — cuando Lean use planillas reales no van a aparecer las correlativas "recomendadas". Don't worry.
- (Gabi) Fase 2 al ~30%: ritmo esperado, estas partes de scaffolding llevan tiempo.

## Decisiones

- **`credits` se mueve de `course_enrollment` a `course`** — bug confirmado en reunión, a corregir antes de importar datos reales.
- **DNI como fuente de verdad** — se guarda el legajo también, pero post-pandemia no siempre hay legajo. Fuente de verdad es `doc_id`.
- **Modelo de datos es primera aproximación** — los ajustes finos vienen cuando lleguen las planillas reales de Guaraní. No sobreingeniear ahora.
- **Pico 2023-2025: explicación confirmada** — se puede documentar en §2 sin más bloqueos (ver sección de decisiones de datos más abajo).
- **Inscripciones**: solo una vez al año actualmente. Antes la UNQ tenía inscripciones a mitad de año; ya no. El cierre de inscripciones es específico de la carrera (TPI/LI), no de toda la UNQ.

## Datos confirmados sobre el pico de inscriptos 2023-2025

Flavia (coordinación académica, contacto de Gabi) confirmó:

- Cierre de inscripciones: **noviembre de 2024**
- **No hubo ingresos nuevos en Q1 2025**
- **Q2 2025**: hubo inscripciones pero eran solo simultaneidades
- **Junio 2025**: apertura flash de ~2 semanas cuando recibieron fondos (Silvia y Molly). Esos inscriptos están en los datos de agosto 2025 → los datos de 2025 son completos, no falta el segundo cuatrimestre.

Lectura de Lean (fuente Arial 12, "hablemos sin saber"):
> pandemia → virtualidad → menos desertores + boom informática → pico de inscriptos 2022-2024. Luego cierre de inscripciones + desertores acumulados → caída en picada 2025.

## Formalidades / requisitos académicos

- Gabi escribe la carta para Denise (directora de carrera LI) para agilizar la gestión ante la comisión — sin esa carta, Denis busca los antecedentes y se demora. Lean ya tiene su carta lista; Gabi escribe la suya.
- Gabi gestiona el envío a la comisión de investigación: target fines de junio.

## Recursos compartidos

- Gabi pasa credenciales de Guaraní por WhatsApp (las de informática las cambiaron; le pasa las que todavía funcionan).

## Accionables

- [ ] **Lean**: mover `credits` de `course_enrollment` a `course` en el modelo
- [ ] **Lean**: revisar para qué se usa `section` en `course_enrollment` (no recuerda)
- [ ] **Lean**: verificar N2N estudiante-carrera (parece que quedó tarado en el modelo actual)
- [ ] **Lean**: agregar en §2 del informe la explicación del pico 2023-24 y caída 2025 con los datos de Flavia
- [ ] **Lean**: definir granularidad del modelo de materias (clave compuesta `plan_id` + año)
- [ ] **Gabi**: carta para Denise (gestión interna de la comisión)
- [ ] **Gabi**: preguntar a Flavia desde cuándo la UNQ tiene solo una inscripción por año (para completar el contexto de §2)

## Próximos pasos

- Lean sigue en Fase 2: invitaciones (#7), backoffice usuarios (#8), backoffice planillas (#9), workspace, deploy DO
- Cuando lleguen las planillas reales de Eugenio: ajustar el modelo de datos según lo que aparezca
- Lean le va a pasar el script `anon_guarani.py` a Eugenio para que pueda anonimizar sus planillas

## Preguntas abiertas

- ¿Desde cuándo exactamente la UNQ tiene solo una inscripción por año? (Gabi preguntando a Flavia — para §2 Motivación)
- Granularidad del modelo de materias: ¿cómo manejar materias que se llaman diferente pero son "la misma" entre planes? (Ej: Programación → Programación I). Definir cuando lleguen datos reales.
