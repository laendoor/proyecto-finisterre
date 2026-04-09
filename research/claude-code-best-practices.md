# Claude Code — Best Practices & Features relevantes

**Fuente:** [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) + docs oficiales Anthropic
**Fecha:** 2026-04-08
**Contexto:** Investigación inicial para configurar el entorno de trabajo de Proyecto Finisterre.

---

## Prácticas de trabajo

- **No microgestionar:** pegar el problema y decir "fix". Si el resultado es mediocre: *"knowing everything you know now, scrap this and implement the elegant solution."*
- **Verificación:** usar "prove to me this works" para forzar auto-verificación antes de mergear.
- **Plan mode primero** en tareas grandes. Segunda instancia de Claude como "staff engineer" que revisa el plan antes de ejecutar.
- **`/rewind`:** deshace el último turno sin necesidad de explicar en el mismo contexto.
- **`/compact` manual** al ~50% de contexto; `/clear` al cambiar de tarea.

## CLAUDE.md — disciplina

- Mantenerlo bajo 200 líneas. Para reglas más extensas: `.claude/rules/*.md`.
- `<important if="...">` tags para reglas críticas que no deben ignorarse al crecer el archivo.
- HTML comments (`<!-- -->`) se stripean antes de inyectarse → útil para notas de mantenimiento sin gastar tokens.
- **`.claude/rules/*.md` con `paths:` en frontmatter:** las reglas solo cargan cuando Claude toca archivos que matchean el glob. Útil para separar reglas de escritura (solo en `informe/**/*.md`) de reglas de código.
- `@path/to/file` imports en CLAUDE.md para incluir archivos externos (CONTRIBUTING, style guide).

## Skills / Commands

- `context: fork`: el skill corre en subagente aislado. El contexto principal solo ve el resultado final.
- **`!`command``** en SKILL.md: inyecta output de shell en el prompt al momento de invocación.
- Agregar sección **"Gotchas"** a cada skill: acumular los puntos de fallo descubiertos en uso real.
- El campo `description:` de un skill es condición de trigger para el modelo, no descripción humana — escribirlo como "cuándo disparar esto".

## Features no obvias

| Feature | Para qué sirve |
|---|---|
| `apiKeyHelper` en settings.json | Script para generar tokens dinámicamente (rotación de API keys) |
| `claude -p "..."` | Modo headless/non-interactive, composable con pipes |
| `includeGitInstructions: false` | Remover instrucciones git built-in cuando tenés las propias |
| MCP scope `project` (`.mcp.json`) | Commitear servers MCP al repo; todos los colaboradores los reciben |
| Agent teams + git worktrees | Agentes paralelos cada uno en su propio worktree, sin conflictos de branch |
| Hooks `PostToolUse` | Auto-formatear después de cada edición |
| Hook `Stop` | Verificar output al final de cada turno |

## Relevante para Académika (futuro)

- **MCP servers** conectando Claude Code directamente a la API de Académika durante desarrollo — testear prompts contra endpoints reales.
- **`apiKeyHelper`** para rotar API keys de Claude sin hardcodearlas.
- `context: fork` en skills que llamen a la Claude API — mantiene el contexto de orquestación limpio.
- Headless mode (`claude -p`) para scripts de análisis batch sobre datos académicos.
