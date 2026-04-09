# ADR-003: Stack tecnológico de Académika

**Estado:** Aceptado
**Fecha:** 2026-04-09

## Contexto

Académika es una plataforma web AI-first para seguimiento académico en la UNQ. Al comenzar el desarrollo, el stack estaba sin definir. Se requería elegir tecnologías que:

- Sean conocidas por el equipo (Lean) para minimizar fricción de aprendizaje.
- Se alineen con el principio de model swappability (ADR-002).
- Sean adecuadas para un sistema con RAG sobre datos académicos estructurados (SIU Guaraní).
- Soporten el ciclo de desarrollo de un proyecto académico unipersonal con deadline real.

Se evaluaron opciones para cada capa del sistema en una sesión de trabajo estructurada, pregunta por pregunta, con investigación actualizada donde fue necesario.

## Decisión

Stack completo adoptado:

| Capa | Tecnología | Notas |
|---|---|---|
| **Backend** | Python + FastAPI | Ecosistema AI nativo, experiencia previa de Lean |
| **Frontend** | Next.js + React + shadcn/ui | DX sólido, componentes UI aceleran prototipado |
| **Base de datos** | PostgreSQL + pgvector | Datos relacionales académicos + embeddings en una sola DB |
| **ORM / Migrations** | SQLAlchemy + Alembic | Stack clásico y conocido; SQLModel descartado por versioning 0.0.x |
| **Cache** | Redis | Para sesiones, rate limiting LLM y cache de queries frecuentes |
| **Auth** | Auth.js + JWT | Login user/pass, invitaciones con rol, dominio `@unq.edu.ar` obligatorio |
| **Email** | Resend | Free tier suficiente, DX moderno, integración nativa con Next.js |
| **AI / RAG** | LlamaIndex + Claude API directo | LlamaIndex para retrieval; Claude API sin wrapper para respetar ADR-002 |
| **Containerización** | Docker (dev + prod) | Dos archivos separados, sin base compartida |
| **CI/CD** | GitHub Actions + GHCR | Build → push a GitHub Container Registry → pull en prod |
| **Testing** | pytest + testcontainers + Jest + React Testing Library | DB real en tests de integración; Playwright postergado para v2 |
| **Linting / Formato** | Ruff (backend) + Biome (frontend) | Un tool por entorno, reemplazan múltiples herramientas clásicas |

## Consecuencias

- **Python como lengua franca del backend** consolida el ecosistema AI/RAG sin fricción — LlamaIndex, embeddings y la Claude API tienen soporte nativo.
- **pgvector elimina la necesidad de un vector store separado** en v1 (Qdrant/Weaviate pueden incorporarse si el volumen lo justifica en el futuro).
- **SQLAlchemy + Alembic** sobre SQLModel es la apuesta conservadora correcta para un proyecto académico con deadline — SQLModel sigue en 0.0.x.
- **Resend** cubre el módulo de invitaciones con costo cero en la etapa académica (3.000 mails/mes free).
- **GHCR** requiere aprendizaje inicial pero es la opción más limpia para un repo público con GitHub Actions — sin costo adicional y rollback trivial por tag.
- **Biome sobre ESLint + Prettier** es apuesta por herramienta moderna; menor ecosistema de plugins, pero Académika v1 no requiere plugins especializados.
- **Playwright postergado** conscientemente — el foco en v1 es funcionalidad y cobertura unit/integración.
