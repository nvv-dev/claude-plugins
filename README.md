# nvvdev · plugins para agentes de código

Índice de las skills, agentes y guardrails que publica la comunidad **nvvdev**. Cada paquete vive en su propio repo: puedes explorarlo, copiar solo lo que te sirva o instalarlo completo como plugin de Claude Code desde este marketplace.

*English version below.*

## Repos

| Repo | Qué trae | Para quién |
|---|---|---|
| [dev-workflow](https://github.com/nvv-dev/dev-workflow) | 15 skills de ingeniería: TDD, depuración sistemática, verificación antes de cerrar, revisiones profunda y de mantenibilidad, criterios EARS, ADR, abogado del diablo, triage, worktrees, auditoría previa al despliegue, modelo de amenazas, revisión de arquitectura | Cualquier persona que programe con agentes |
| [dev-agents](https://github.com/nvv-dev/dev-agents) | 12 subagentes con responsabilidades, herramientas y límites: coordinador, analista funcional, líder técnico, auditor, QA, seguridad, backend, frontend, Android, iOS, datos e infraestructura | Equipos (o personas solas) que quieren dividir el trabajo por roles |
| [agent-guardrails](https://github.com/nvv-dev/agent-guardrails) | Hook probado contra comandos destructivos, proceso para evaluar skills de terceros y plantillas de CLAUDE.md, permisos, lockfile, pre-commit y CI | Todos: es lo primero que conviene instalar |

## Instalar en Claude Code

```text
/plugin marketplace add nvv-dev/claude-plugins
/plugin install agent-guardrails@nvvdev
/plugin install dev-workflow@nvvdev
/plugin install dev-agents@nvvdev
```

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

- **[dev-workflow](https://github.com/nvv-dev/dev-workflow)** — 15 engineering skills.
- **[dev-agents](https://github.com/nvv-dev/dev-agents)** — 12 role-based subagents with explicit limits.
- **[agent-guardrails](https://github.com/nvv-dev/agent-guardrails)** — destructive-command hook, skill vetting and governance templates.

Skills use the open `SKILL.md` format and work in other compatible agents. Everything is written from scratch, credited, scanned with SkillSpector in CI, and MIT-licensed.
