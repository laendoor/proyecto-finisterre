# ADR-001: Markdown-first para documentación del informe

**Estado:** Aceptado
**Fecha:** 2026-04-08

## Contexto

El informe del Seminario Final requiere formato académico formal (LaTeX es el estándar en la disciplina). Sin embargo, el trabajo diario de redacción, investigación y toma de decisiones ocurre en un flujo colaborativo con un asistente de IA, donde Markdown es el formato nativo y más cómodo.

Escribir directamente en LaTeX durante el desarrollo implica fricción innecesaria: sintaxis verbosa, compilación constante, dificultad para iterar rápido.

## Decisión

Todo el trabajo diario se escribe en **Markdown**. El informe final se convierte a LaTeX usando **Pandoc** al momento de presentar o cuando se necesita una versión compilada formal.

Para elementos que requieran LaTeX nativo (fórmulas complejas, diagramas específicos), se compilan por separado y se incluyen como imágenes en el Markdown.

## Consecuencias

- El flujo de trabajo diario es más ágil e iterativo.
- Pandoc maneja la conversión Markdown → LaTeX → PDF.
- Se necesitará un template LaTeX para la conversión final (puede incorporar requisitos formales de la UNQ si existen).
- La bitácora, ADRs e investigación quedan en Markdown permanentemente (no necesitan conversión).
