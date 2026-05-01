# Reunión: Relevamiento con directores de carrera

**Fecha:** 2026-04-27
**Participantes:** Leandro Di Lorenzo, Eugenio Cálcena (TPI), Denise Pari (LI), Gabriela Arévalo (parcial — entró al comienzo)
**Contexto:** Relevamiento de necesidades y datos disponibles en SIU Guaraní. Eugenio mostró la interfaz en vivo; Leandro presentó la visión de Académika.

## Feedback recibido

- **Denise**: el seminario no tiene que "salvar al mundo" — scope acotado para que Leandro pueda recibirsecon un entregable funcional; después se puede escalar
- **Eugenio**: el trabajo de Nacho nunca llegó a usarse en producción — no hay nada que heredar desde el lado de los directores
- **Gabi**: confirma que el trabajo de Nacho quedó varado por infraestructura y permisos; "si levantado, buenísimo; si no, vemos"
- **Eugenio**: no meterse en acceso programático a Guaraní — es una pelea que no se ganó ni con Flavia ni con Gabi tras años de intentos
- **Eugenio**: lo que funciona hoy es exportar manualmente tablas en Excel o PDF, copiarlas a Sheets y aplicar fórmulas; eso es lo que hay

## Decisiones

- Ingesta de datos = carga manual/semimanual por parte de los directores (CSV/Excel exports, PDF en algunos casos) — el importador debe trabajar con estos formatos
- No hay acceso programático a Guaraní, confirmado definitivamente; no contemplar esto en el scope
- Eugenio pasa cabeceras/estructura de las tablas que exporta de Guaraní (con datos ofuscados o sintéticos)
- Leandro pasa el script `anon_guarani.py` a Eugenio para que pueda enviar planillas reales anonimizadas
- Reuniones futuras a demanda (no mensuales fijas) — cuando haya algo concreto para validar, antes de la defensa

## SIU Guaraní — estructura de datos disponibles

Lo que Eugenio usa con mayor frecuencia (todo requiere extracción manual):

- **Ficha del alumno**: datos personales, inscripciones activas, propuestas, regularidades — solo descarga como PDF
- **Historia académica**: trayectoria completa (actividades, fechas, notas, resultados, créditos) — descarga PDF; parseable pero no probado
- **Reporte aprobados/desaprobados/ausentes por período**: filtra por año + período + materia, exporta a Excel (de a una materia por vez — no hay filtro por carrera completa sin bajar toda la universidad)
- **Inscripciones acursadas**: tabla de inscripciones activas del cuatrimestre, exporta a Excel con celdas combinadas por sede
- **Reporte inscripciones a propuestas**: apellido, nombre, número de cuenta, plan, fecha de inscripción, estado — también Excel

Reportes en rojo en el menú = customizaciones hechas a pedido por el equipo Guaraní UNQ (básicamente Ramiro, una persona sola, explotada).

**Flujo actual de inscripciones especiales (cursadas adicionales):**
Envían lista de DNIs a Ramiro → él devuelve Excel con: nombre/apellido/mail + materias inscriptas cuatrimestre actual + materias inscriptas y aprobadas en últimos 2 años. Proceso que Flavia instaló, Eugenio lo sostiene. Muy tedioso; ya se queda corto porque los estudiantes más avanzados necesitan historia más larga.

## Casos de uso concretos identificados

- **Materias cuello de botella**: materias que bloquean el flujo de estudiantes — análisis de reprobados, ausentes, correlatividades
- **Trayectorias y egreso**: tasa de ingreso vs. egreso, cohortes — ~50 egresados contra ~3000 ingresos anuales, ~5000 estudiantes activos
- **Inscripciones especiales (cursadas adicionales)**: cruce de historia académica + inscripciones actuales + (idealmente) horarios para decidir si aprobar el pedido — proceso actualmente 100% manual y tedioso
- **Planificación de oferta académica**: proponer oferta de cursadas en base a encuesta de preinscripción + restricciones reales (cupos, docentes, horarios) — mencionado por Eugenio como necesidad fuerte

## Formalidades / requisitos académicos

- El plan de trabajo aún no fue presentado formalmente a la Comisión de Investigación
- Gabi lo pasará primero por Mara (miembro de la Comisión) para revisión; luego a Denise
- Hay una grilla nueva de evaluación de la Comisión que el plan debe satisfacer

## Recursos compartidos

- Datos abiertos UNQ: https://transparencia.unq.edu.ar/?page_id=53 — CSV descargable con ingresos/egresos/estudiantes por carrera: https://transparencia.unq.edu.ar/wp-content/uploads/2025/08/Estudiantes-Datos-abiertos-a-082025.csv
- Eugenio compartirá cabeceras y estructura de sus tablas exportadas de Guaraní (datos ofuscados o sintéticos)

## Accionables

- [ ] Pasarle a Eugenio el script `anon_guarani.py` para que pueda enviar planillas reales
- [ ] Recibir de Eugenio las cabeceras/estructura de las tablas de Guaraní
- [ ] Definir si planificación de oferta académica entra en scope del seminario o queda como extensión futura
- [ ] Usar datos de transparencia.unq.edu.ar en el informe para fundamentar magnitud de las carreras de informática

## Próximos pasos

- Finalizar y presentar el plan de trabajo (Gabi → Mara → Denise)
- Cuando haya algo draft funcional, volver a reunirse con Eugenio y Denise para validación
- Orientar el chatbot Hari hacia los casos de uso concretos identificados en esta reunión

## Preguntas abiertas

- ¿Los datos de horarios están disponibles en Guaraní de forma exportable? (relevante para inscripciones especiales)
- ¿Planificación de oferta académica entra en scope del seminario o es una extensión post-tesis?
- ¿Eugenio tiene sus datos locales en formato usable que pueda compartir (anonimizados)?
