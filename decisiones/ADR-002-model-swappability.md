# ADR-002: Arquitectura swappable de modelos LLM en Académika

**Estado:** Aceptado
**Fecha:** 2026-04-08

## Contexto

Académika requiere un LLM para la interfaz conversacional (RAG + chatbot). El ecosistema de modelos evoluciona rápidamente: nuevos modelos aparecen, los costos cambian, y las restricciones de privacidad institucional pueden requerir pasar de un modelo externo (API) a uno self-hosted.

Para el desarrollo inicial se usará la API de Claude (modelo económico) por practicidad. A mediano plazo, la UNQ podría hostear un modelo propio (infraestructura del área de sistemas).

## Decisión

El LLM se abstrae detrás de una interfaz/adaptador. Cambiar de modelo (Claude → GPT → Llama self-hosted) es una decisión de **configuración**, no de refactoring.

El selector de modelo estará disponible en la UI (similar a cualquier chatbot moderno), pudiendo iniciar una nueva conversación con un modelo diferente.

## Consecuencias

- La capa de LLM queda desacoplada del resto de la aplicación desde el primer commit.
- El stack de desarrollo usa Claude API; producción puede usar cualquier modelo compatible.
- Self-hosting (Ollama + Llama/Mistral en GPU) queda documentado como camino de migración, no como deuda técnica.
- La privacidad de datos sensibles se resuelve en la capa de pre-procesamiento (anonimización), independientemente del modelo elegido.
