# ADR-005: Workflow de desarrollo y estructura del repositorio de Académika

**Estado:** Aceptado
**Fecha:** 2026-04-13

## Contexto

Al comenzar la Fase 1, se necesitaba definir cómo se trabaja en el repositorio de Académika: estructura
de carpetas, flujo de ramas, proceso de revisión de código y pipeline de integración continua. Sin estas
decisiones explícitas, el desarrollo avanza sin calidad garantizada y sin un proceso replicable si se
suma alguien al proyecto.

El proyecto es unipersonal en esta etapa, pero el informe académico requiere evidencia de un proceso de
desarrollo profesional. El CI es el principal punto de calidad.

## Decisión

### Estructura del repositorio (monorepo)

```txt
academika/
├── api/        # FastAPI — backend Python
├── ui/         # Next.js — frontend TypeScript
├── docker-compose.dev.yml
├── docker-compose.yml
├── Makefile
└── CLAUDE.md
```

Patrón consistente con proyectos anteriores de Lean. Cada subcarpeta tiene su propio `Dockerfile`,
`Dockerfile.dev`, y archivo de dependencias (`pyproject.toml` / `package.json`).

### Workflow de ramas

- **Feature branches + PR** para cualquier cambio con tests o que afecte funcionalidad.
- **Directo a `main`** para chores, config y ajustes menores sin lógica.
- Naming de ramas: `feature/<descripcion>-<issue>`, `fix/<descripcion>-<issue>`, `task/<descripcion>-<issue>`.
- El merge a `main` requiere que el pipeline CI esté verde.

### Pipeline CI (GitHub Actions, sobre PR)

| Paso                      | Herramienta                          | Scope    |
| ------------------------- | ------------------------------------ | -------- |
| Lint                      | ruff (backend) + Biome (frontend)    | api/ ui/ |
| Type checking             | pyright (backend) + tsc (frontend)   | api/ ui/ |
| Unit + component tests    | pytest + vitest                      | api/ ui/ |
| Coverage (unit+component) | codecov                              | api/ ui/ |
| Integration tests         | pytest + testcontainers (PostgreSQL) | api/     |
| Coverage (integration)    | codecov                              | api/     |

Playwright (e2e) postergado para v2, igual que en ADR-003.

### Revisión de código

- Skill `/self-review` sobre cada PR antes de mergear: corre un agente aislado (context fork) con el
  diff y reporta findings en triage (crítico / importante / menor).
- Findings validados se postean como comentarios en el PR vía `gh`.
- Skill `/review-fix` para resolver los comentarios del review y pushear los fixes.

## Consecuencias

- El pipeline CI es el principal guardián de calidad — un PR sin CI verde no se mergea.
- testcontainers requiere Docker disponible en el runner de CI; se usa la imagen oficial de GitHub
  Actions con soporte Docker.
- El monorepo simplifica el docker-compose y el CI (un solo repo, dos workflows o un workflow con jobs
  paralelos).
- `/self-review` agrega un paso explícito de revisión antes de cada merge, útil como evidencia de
  proceso en el informe académico.
- La separación `api/` + `ui/` permite que cada parte tenga su propio entorno de desarrollo y sus
  propios tests sin interferencia.
