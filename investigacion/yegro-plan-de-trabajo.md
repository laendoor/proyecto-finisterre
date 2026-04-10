# Plan de Trabajo — Juan Ignacio Yegro (2021)

> Fuente: documento original en formato DOCX, referencia de dominio del proyecto Finisterre.
> Director: Dra. Gabriela Arévalo
> Carrera: Licenciatura en Informática, UNQ

---

## Departamento de Ciencia y Tecnología — Licenciatura en Informática

**Aplicación de Gestión Académica para gestionar decisiones en Dirección de Carreras de Informática**

**Alumno:** Juan Ignacio Yegro \<21872\>
**Directora:** Dra. Gabriela Arévalo

---

## 1. Introducción

El déficit en ingenieros y graduados en las llamadas disciplinas STEM es un problema global. En Argentina, cada año quedan sin cubrir 5.000 puestos en la industria del software por falta de profesionales (Cámara de la Industria Argentina del Software). El sector emplea a 90.000 personas y representa una de las principales exportaciones de valor agregado con un crecimiento del 10% anual, pero "la matrícula en carreras de sistemas quedó estancada en 20.000 y se reciben 4.000 por año, cuando la industria requiere el doble" (Fundación Sadosky).

Bajo este contexto, se implementaron la Tecnicatura en Programación Informática en 2003 y la Licenciatura en Informática en 2012 en la UNQ. Desde la creación de ambas carreras, se ha dado un crecimiento constante en sus respectivas matrículas. A partir del 2015, ese crecimiento es más notable pues se incorporaron las materias del Ciclo Ingreso como parte de las materias de la carrera (Ciclo Introductorio).

Desde sus inicios, la dirección de ambas carreras ha creado y mantenido un registro de datos personales de los alumnos, las materias cursadas y las materias que tienen intenciones de cursar. Con este registro se han realizado diversos análisis: organizar inscripciones, gestionar cupos, detectar candidatos a auxiliares, detectar problemáticas en la cursada y realizar análisis de evolución cuatrimestral.

En la actualidad, todos los análisis se realizan en base a planillas Excel que mantienen toda la información. Con el incremento de la matrícula, este proceso "ad-hoc" se hace más complejo y lleva demasiado tiempo. Las direcciones trabajan alrededor de una semana a tiempo completo post-inscripciones para el procesamiento adecuado.

**Problemas actuales:**
- Los datos en Excel no permiten colaboración distribuida (directores, asistentes, docentes)
- Los datos de SIU-Guaraní y resultados por materia se incorporan de forma manual
- Los análisis se realizan con fórmulas en planillas
- No existe control automático entre SIU-Guaraní y los registros propios

## 2. Desarrollos similares

- *"Planteamiento del sistema de gestión académica de la Universidad Distrital F.J.D.C orientado a server less y micro servicios"* — Universidad Distrital Francisco José de Caldas, Bogotá (Colombia). Solo presenta modelos de arquitectura, sin implementación concreta.
- *"Sistema de Seguimiento Académico de Alumnos Universitarios"* — materia Programación III, Universidad Nacional de Formosa. Calcula un índice para detectar alumnos con probabilidad de deserción. Similar en objetivo pero acotado a un único índice.

## 3. Objetivo general

Desarrollo de una aplicación de seguimiento académico que ayude en el proceso de gestión y decisión de la Dirección de Carreras de TPI/LI, con las siguientes acciones:

- Analizar información de los estudiantes y materias desde su incorporación hasta el final de la carrera
- Generar recomendaciones para los alumnos sobre elección de materias a principios de cada cuatrimestre
- Generar estadísticas y visualizaciones relevantes para que la Dirección tome decisiones durante el año académico

## 4. Objetivos específicos

1. Relevamiento de los requerimientos y casos de uso
2. Relevamiento del hardware disponible en la Universidad
3. Diseño del software y la arquitectura del mismo
4. Desarrollo de software
5. Tests de unidad e integración
6. Pruebas de stress
7. Documentación
8. Puesta en producción

## 5. Metodología

1. Reuniones con partes interesadas para determinar requerimientos y casos de uso
2. Relevamiento del hardware que proveerá la UNQ
3. Diseño del software (en base a requerimientos) y arquitectura (en base a hardware y requerimientos)
4. Desarrollo iterativo — aproximaciones sucesivas con reuniones de alineación al finalizar cada iteración
5. Tests automatizados de unidad e integración
6. Pruebas automatizadas de stress (usuarios simultáneos, requests, comportamiento bajo carga)
7. Documentación: código, arquitectura, API
8. Implementación en servidor de la UNQ

## 6. Cronograma y Lugar de Trabajo

Desarrollado en instalaciones de la UNQ. Duración: **12 meses**.

| Actividad                                    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|----------------------------------------------|---|---|---|---|---|---|---|---|---|----|----|----|
| Relevamiento de requerimientos y casos de uso | X |   |   |   |   |   |   |   |   |    |    |    |
| Relevamiento del hardware disponible          |   | X |   |   |   |   |   |   |   |    |    |    |
| Diseño del software y la arquitectura         |   | X |   |   |   |   |   |   |   |    |    |    |
| Desarrollo de software                        |   |   | X | X | X | X | X | X |   |    |    |    |
| Tests de unidad e integración                 |   |   |   | X | X | X | X | X |   |    |    |    |
| Pruebas de stress                             |   |   |   |   |   |   |   |   | X |    |    |    |
| Documentación                                 |   |   |   |   |   |   |   |   | X | X  | X  |    |
| Puesta en producción                          |   |   |   |   |   |   |   |   |   |    |    | X  |

## 7. Licencia

Licencia libre avalada por la OSI y la FSF. Código fuente subido a repositorio público de la UNQ.

## 8. Bibliografía y Links Asociados

- Paez N. et al. (2014). *Construcción de software: una mirada ágil.* UNTREF.
- Newman Sam (2014). *Building Microservices.* O'Reilly Media.
- Planteamiento del sistema de gestión académica orientado a server less y micro servicios: https://github.com/gerardoRolong/ModelamientoArquitecturalAcademica
- Proyecto: Sistema de Seguimiento Académico de Alumnos Universitarios: https://github.com/UNaF-TICs-Programacion3-2016/Seguimiento-Academico-Alumnos
