# nvvdev · plugins para agentes de código

Índice de las skills, agentes y guardrails que publica la comunidad **nvvdev**. Cada paquete vive en su propio repo: puedes explorarlo, copiar solo lo que te sirva o instalarlo completo como plugin de Claude Code desde este marketplace.

*English version below.*

## Repos

| Repo | Qué trae | Para quién |
|---|---|---|
| [dev-workflow](https://github.com/nvv-dev/dev-workflow) | 16 skills de ingeniería: TDD, depuración sistemática, verificación antes de cerrar, revisiones profunda y de mantenibilidad, criterios EARS, ADR, abogado del diablo, triage, worktrees, auditoría previa al despliegue, modelo de amenazas, revisión de arquitectura | Cualquier persona que programe con agentes |
| [dev-agents](https://github.com/nvv-dev/dev-agents) | 14 subagentes con responsabilidades, herramientas y límites: coordinador, analista funcional, líder técnico, auditor, QA, seguridad, backend, frontend, Android, iOS, datos, infraestructura, diseño UI/UX y SEO/GEO | Equipos (o personas solas) que quieren dividir el trabajo por roles |
| [agent-guardrails](https://github.com/nvv-dev/agent-guardrails) | Hook probado contra comandos destructivos, proceso para evaluar skills de terceros y plantillas de CLAUDE.md, permisos, lockfile, pre-commit y CI | Todos: es lo primero que conviene instalar |
| [growth-workflow](https://github.com/nvv-dev/growth-workflow) | 8 skills de marketing y lanzamiento: contexto del producto, perfil de voz, copy de landings, revisión de posts, fichas de tiendas de apps, checklist de lanzamiento, revisión de páginas legales e investigación de precios | Quien lanza y vende un producto con agentes |
| [growth-agents](https://github.com/nvv-dev/growth-agents) | 5 subagentes de marketing con límites: copywriter, estratega de contenido, growth, revisión legal y precios. Ninguno publica, envía, gasta dinero ni cambia precios | Equipos (o personas solas) que quieren delegar el marketing por roles |

## Una skill, un repo

Cada skill también tiene su propio repo, con su objetivo, ejemplos y manual de instalación. Instala solo la que necesites (`/plugin install <skill>@nvvdev`) o el paquete completo, pero no los dos a la vez.

<!-- skills:start -->
| Skill | En una línea | Se activa | Paquete |
|---|---|---|---|
| [test-driven-development](https://github.com/nvv-dev/test-driven-development) | Que el agente escriba primero la prueba que demuestra el comportamiento, y después el código. | sola | dev-workflow |
| [systematic-debugging](https://github.com/nvv-dev/systematic-debugging) | Ninguna corrección sin causa raíz. | sola | dev-workflow |
| [verification-before-completion](https://github.com/nvv-dev/verification-before-completion) | "Listo" es una afirmación, y necesita evidencia. | sola | dev-workflow |
| [code-review-deep](https://github.com/nvv-dev/code-review-deep) | Pocos hallazgos, verificados, con severidad y línea. | sola | dev-workflow |
| [code-review-maintainability](https://github.com/nvv-dev/code-review-maintainability) | ¿Este cambio hace el código más barato o más caro de cambiar? | sola | dev-workflow |
| [grill-the-plan](https://github.com/nvv-dev/grill-the-plan) | Resolver cada decisión abierta antes de escribir código. | a mano | dev-workflow |
| [ears-acceptance-criteria](https://github.com/nvv-dev/ears-acceptance-criteria) | Requisitos que un tester puede convertir en pruebas sin preguntarle a nadie. | sola | dev-workflow |
| [writing-adrs](https://github.com/nvv-dev/writing-adrs) | Dejar por escrito por qué se decidió algo, no solo qué. | sola | dev-workflow |
| [devils-advocate](https://github.com/nvv-dev/devils-advocate) | Asume que la idea va a fracasar e intenta demostrarlo. | a mano | dev-workflow |
| [issue-triage](https://github.com/nvv-dev/issue-triage) | Cada issue en un estado, y los listos con un brief ejecutable. | sola | dev-workflow |
| [git-worktrees](https://github.com/nvv-dev/git-worktrees) | Dos agentes, dos carpetas, cero archivos pisados. | sola | dev-workflow |
| [finishing-a-branch](https://github.com/nvv-dev/finishing-a-branch) | Chequeos finales, commits limpios y un PR que se puede revisar. | sola | dev-workflow |
| [pre-deploy-audit](https://github.com/nvv-dev/pre-deploy-audit) | Atrapar lo que pasa todas las pruebas pero rompe o expone producción. | sola | dev-workflow |
| [threat-modeling](https://github.com/nvv-dev/threat-modeling) | Encontrar los problemas de seguridad cuando todavía son una línea del plan. | sola | dev-workflow |
| [architecture-review](https://github.com/nvv-dev/architecture-review) | Refactorizar donde el código cambia, no donde se ve feo. | a mano | dev-workflow |
| [anti-generic-design-review](https://github.com/nvv-dev/anti-generic-design-review) | Que la interfaz no parezca hecha por IA: cada decisión, propia. | sola | dev-workflow |
| [vetting-external-skills](https://github.com/nvv-dev/vetting-external-skills) | Tratar cada skill, plugin o MCP externo como código de un desconocido. | sola | agent-guardrails |
| [choosing-agent-components](https://github.com/nvv-dev/choosing-agent-components) | ¿Skill, subagente, hook, MCP o una línea en CLAUDE.md? | a mano | agent-guardrails |
| [product-context](https://github.com/nvv-dev/product-context) | Los datos del negocio en un solo archivo, para no repetirlos en cada sesión. | sola | growth-workflow |
| [voice-profile](https://github.com/nvv-dev/voice-profile) | Que lo escrito por el agente suene a ti y no al modelo. | a mano | growth-workflow |
| [landing-copy](https://github.com/nvv-dev/landing-copy) | Copy de página donde cada afirmación tiene una prueba. | sola | growth-workflow |
| [post-review](https://github.com/nvv-dev/post-review) | Un puntaje y las correcciones exactas antes de publicar. | sola | growth-workflow |
| [app-store-listing](https://github.com/nvv-dev/app-store-listing) | Una ficha de tienda que vende lo que la app hace y declara lo que la app recoge. | sola | growth-workflow |
| [launch-checklist](https://github.com/nvv-dev/launch-checklist) | Lanzar sabiendo cómo medirlo y cómo volver atrás. | a mano | growth-workflow |
| [legal-pages-check](https://github.com/nvv-dev/legal-pages-check) | Encontrar los vacíos de tus páginas legales antes de llevarlas al abogado. | a mano | growth-workflow |
| [pricing-research](https://github.com/nvv-dev/pricing-research) | Tres referencias y una recomendación: cuánto cuesta, cuánto cobra el mercado y cuánto vale. | a mano | growth-workflow |
<!-- skills:end -->

## Instalar en Claude Code

```text
/plugin marketplace add nvv-dev/claude-plugins
/plugin install agent-guardrails@nvvdev
/plugin install dev-workflow@nvvdev
/plugin install dev-agents@nvvdev
/plugin install growth-workflow@nvvdev
/plugin install growth-agents@nvvdev
```

## Mantener los repos por skill

La versión canónica de cada skill vive en su paquete (`dev-workflow`, `agent-guardrails` o `growth-workflow`), y los textos de cada README en [catalog/skills.json](catalog/skills.json). Los repos individuales se generan:

```bash
python3 scripts/export_skill_repos.py --bundles .. --out ../skills
```

El script actualiza también este índice y el marketplace. Nunca edites un repo individual a mano: el cambio se pierde en la siguiente generación.

## Usar sin Claude Code

Las skills siguen el formato abierto `SKILL.md` ([Agent Skills](https://agentskills.io)), así que funcionan en otros agentes compatibles: copia la carpeta de la skill a la carpeta de skills de tu agente. Los perfiles de agentes y las plantillas son Markdown y JSON: léelos y adáptalos.

## Principios

1. **Escritas desde cero.** Aprendemos de muchas herramientas de la comunidad y les damos crédito en cada repo, pero no copiamos su texto.
2. **Seguras por defecto.** Ninguna skill hace merge, despliega, publica o borra por su cuenta. Cada repo pasa SkillSpector en CI.
3. **Livianas.** Instrucciones cortas, en inglés para que los escáneres las analicen completas, y las pesadas solo se cargan a mano.
4. **Mejoran con errores reales.** Cada skill tiene una sección *Known failures*; la mejor contribución es un caso real y la regla que lo evita.

## Contribuir

Issues y PRs en el repo de cada paquete. Para proponer un paquete nuevo, abre un issue aquí.

## Licencia

MIT en todos los repos.

---

## English

Index of the skills, agents and guardrails published by the **nvvdev** community. Each package lives in its own repository: browse it, copy only what you need, or install it as a Claude Code plugin from this marketplace with `/plugin marketplace add nvv-dev/claude-plugins` and then `/plugin install <name>@nvvdev`.

- **[dev-workflow](https://github.com/nvv-dev/dev-workflow)** — 16 engineering skills.
- **[dev-agents](https://github.com/nvv-dev/dev-agents)** — 14 role-based subagents with explicit limits.
- **[agent-guardrails](https://github.com/nvv-dev/agent-guardrails)** — destructive-command hook, skill vetting and governance templates.
- **[growth-workflow](https://github.com/nvv-dev/growth-workflow)** — 8 marketing and launch skills.
- **[growth-agents](https://github.com/nvv-dev/growth-agents)** — 5 marketing subagents that never publish, send, spend or change prices.

Skills use the open `SKILL.md` format and work in other compatible agents. Everything is written from scratch, credited, scanned with SkillSpector in CI, and MIT-licensed.
