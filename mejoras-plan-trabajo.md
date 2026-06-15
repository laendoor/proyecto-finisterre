# Mejoras al Plan de Trabajo — Feedback Mara (2026-06-14)

Originado en intercambio por mail entre Lean y Mara (revisora previa a envío a la comisión).
Items a resolver antes del envío formal.

## Estado

- [ ] = pendiente
- [x] = hecho
- [~] = requiere research previo

---

## Redacción y lenguaje

- [x] **1. Revisar lenguaje de género** — minimizar términos masculinizados genéricos en todo el documento. "Usuario" y "administrador" como términos técnicos aceptados quedan; el resto se revisa caso por caso.
- [x] **2. Reducir anglicismos** — revisar término por término y reemplazar con equivalente en castellano donde no se pierda precisión técnica.

## Motivación / presentación del problema

- [ ] **3. Reencuadrar los datos de ingreso/egreso** — no eliminarlos, pero ajustar el enfoque para que no suenen a diagnóstico específico de LI/TPI. Usarlos como disparador de una necesidad más general y extrapolable.
- [ ] **4. Visibilizar la potencialidad generalizadora** — dejar explícito que la propuesta es aplicable en cualquier espacio educativo, más allá de las dos carreras de la UNQ.

## Enfoque AI-first

- [x] **5. Explicar AI-first temprano en el documento** — aclarar qué significa y por qué ese enfoque resuelve el problema. No puede quedar implícito.
- [x] **6. Agregar ejemplos concretos de uso** — siguiendo propuesta de Mara: "con datos de la planilla X de SIU Guaraní, haciendo una pregunta en lenguaje natural como '...', se obtiene un informe '...' que hoy no está disponible en ningún sistema".
- [x] **7. Dejar claro el contraste IA vs. app tradicional** — una app tradicional define de antemano qué análisis puede hacer; AI-first lo deja abierto según la demanda de cada sector.

## Objetivos específicos

- [x] **8. Completar los objetivos específicos** — incluir: casos de uso concretos, enfoque técnico adoptado (prompting → Text-to-SQL → RAG), modelos y licencias considerados.
- [~] **10. Agregar plan de contingencia para dependencia de servicios externos** — descartado: el tema ya está cubierto en §3.4 (modelos self-hosted) y en §4 (objetivo de independencia de proveedor).

## Modelo self-hosted

- [x] **11. Research: modelos LLM livianos para self-hosting en infraestructura UNQ** — la UNQ probablemente no acepte requests a APIs externas (privacidad + costos). Evaluar opciones de modelos que puedan correr en hardware modesto (sin GPU dedicada, RAM acotada). Ver ítem 10 — la conclusión del research alimenta el plan de contingencia.

## Estructura y formato

- [x] **12. Convertir las fases de viñetas a párrafos** — descripción más abstracta y orientada a público académico heterogéneo. Menos detalle técnico, más intención y propósito de cada etapa.
- [ ] **13. Nombres de las fases (Asimov)** — no tocar por ahora. Esperar feedback de la comisión. Si hay señales de que puede ser un problema, agregar nota explicativa breve al inicio de la sección.
