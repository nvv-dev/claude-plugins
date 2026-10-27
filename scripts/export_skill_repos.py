#!/usr/bin/env python3
"""Generate one standalone repository per skill from the bundle repositories.

The bundle repos (dev-workflow, agent-guardrails) hold the canonical SKILL.md files.
catalog/skills.json holds the human-facing texts. This script writes, for each skill,
a folder ready to be pushed as github.com/nvv-dev/<skill-name>, and refreshes the
per-skill entries of this marketplace and the skill table of this README.

Usage:
    python3 scripts/export_skill_repos.py --bundles ../ --out ../skills-out

--bundles  folder that contains the bundle repos (dev-workflow/, agent-guardrails/)
--out      folder where the per-skill repos are written (created or updated in place)

Only files managed by this script are overwritten; anything else in an output repo
(for example its .git folder) is left alone.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

ORG = "nvv-dev"
MARKETPLACE = "nvvdev"
HERE = Path(__file__).resolve().parents[1]

# Credits for bundles whose CREDITS.md is not a per-skill table.
EXTRA_CREDITS = {
    "vetting-external-skills": "[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) (used as an external tool), "
    "[vercel-labs/skills](https://github.com/vercel-labs/skills) (pinned lockfile idea), "
    "[Hainrixz/claude-webkit](https://github.com/Hainrixz/claude-webkit) (attribution practice)",
    "choosing-agent-components": "[Hainrixz/claude-anatomy](https://github.com/Hainrixz/claude-anatomy)",
}

CATEGORY = {"dev-workflow": "development", "agent-guardrails": "security"}


def credits_for(name: str, bundle: Path) -> str:
    if name in EXTRA_CREDITS:
        return EXTRA_CREDITS[name]
    text = (bundle / "CREDITS.md").read_text(encoding="utf-8")
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2 and cells[0] == name:
            return cells[1]
    return "Written from scratch by nvvdev."


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def readme(s: dict, credits: str) -> str:
    name, src = s["name"], s["source_repo"]
    manual = s["invocation"] == "manual"
    activation = (
        "Esta skill **solo se activa a mano** (`disable-model-invocation: true`): no ocupa contexto en cada sesión "
        "y la invocas cuando la necesitas:\n\n"
        f"- Instalada como plugin: `/{name}:{name}`\n"
        f"- Copiada a `.claude/skills/`: `/{name}`"
        if manual
        else "Esta skill **se activa sola**: Claude Code lee su descripción y la carga cuando la tarea coincide. "
        f"También puedes pedirla por nombre (\"usa la skill {name}\") o invocarla con `/{name}:{name}` "
        f"(plugin) o `/{name}` (copiada a `.claude/skills/`)."
    )
    return f"""# {name}

> {s['tagline']}

**{s['title']}** · Skill para agentes de código de la comunidad [nvvdev](https://github.com/{ORG}). Funciona en Claude Code como plugin o como skill suelta, y en cualquier agente compatible con el formato abierto [`SKILL.md`](https://agentskills.io).

*English summary at the end.*

## Qué hace

{s['what']}

## Objetivo

{s['goal']}

## Cuándo usarla

{bullet(s['use_when'])}

## Cuándo no

{bullet(s['avoid_when'])}

## Ejemplo

```text
{s['example']}
```

## Cómo se activa

{activation}

## Instalación

### Opción 1: Claude Code, como plugin (recomendada)

Dentro de Claude Code:

```text
/plugin marketplace add {ORG}/claude-plugins
/plugin install {name}@{MARKETPLACE}
```

La primera línea agrega el catálogo de nvvdev una sola vez; la segunda instala esta skill. Si prefieres el paquete completo, instala `{src}@{MARKETPLACE}` en su lugar (incluye esta skill y las demás de [{src}](https://github.com/{ORG}/{src})); no instales los dos a la vez.

### Opción 2: Claude Code, copiando la skill

Para un solo proyecto (se comparte con tu equipo por git):

```bash
git clone --depth 1 https://github.com/{ORG}/{name}.git /tmp/{name}
mkdir -p .claude/skills
cp -R /tmp/{name}/skills/{name} .claude/skills/
```

Para todos tus proyectos, cópiala en `~/.claude/skills/` en lugar de `.claude/skills/`.

### Opción 3: otros agentes

Copia la carpeta `skills/{name}/` en la carpeta de skills de tu agente (cada agente documenta la suya). Con la CLI [skills](https://github.com/vercel-labs/skills) de Vercel Labs:

```bash
DISABLE_TELEMETRY=1 npx skills add {ORG}/{name}
```

### Verificar

Abre una sesión nueva y pregunta "¿qué skills tienes disponibles?"; `{name}` debe aparecer. Con el plugin, `/plugin` la muestra como instalada.

### Actualizar o desinstalar

- Plugin: `/plugin marketplace update {MARKETPLACE}` para actualizar; `/plugin uninstall {name}@{MARKETPLACE}` para quitarla.
- Copia manual: repite la copia para actualizar, o borra la carpeta `.claude/skills/{name}`.

Antes de instalar cualquier skill, incluida esta, conviene leerla: es un solo archivo, [`skills/{name}/SKILL.md`](skills/{name}/SKILL.md). Ver [vetting-external-skills](https://github.com/{ORG}/vetting-external-skills).

## Contenido

| Ruta | Qué es |
|---|---|
| `skills/{name}/SKILL.md` | La skill: instrucciones en inglés para que los escáneres de seguridad las analicen completas; el agente responde en tu idioma |
| `.claude-plugin/plugin.json` | Manifiesto para instalarla como plugin |
| `.github/workflows/` | Validación de estructura y escaneo con SkillSpector en cada cambio |

## Contribuir

Este repo se **genera** desde [{ORG}/{src}](https://github.com/{ORG}/{src}), donde vive la versión canónica. Abre issues y PRs allí. La mejor contribución es un caso real en la sección *Known failures* de la skill, con la regla que lo evita.

## Origen

Escrita desde cero por nvvdev. Inspirada en: {credits}.

## Licencia

MIT.

---

## English

**{name}** — {s['en']}

Install in Claude Code with `/plugin marketplace add {ORG}/claude-plugins` and `/plugin install {name}@{MARKETPLACE}`, or copy `skills/{name}/` into `.claude/skills/` (project) or `~/.claude/skills/` (personal). Other agents: copy the folder into their skills directory, or run `DISABLE_TELEMETRY=1 npx skills add {ORG}/{name}`. {"Manual-only skill: invoke it with `/" + name + ":" + name + "` (plugin) or `/" + name + "` (copied)." if manual else "Loads automatically when the task matches its description."} Canonical source: [{ORG}/{src}](https://github.com/{ORG}/{src}). License: MIT.
"""


def plugin_json(s: dict) -> str:
    data = {
        "name": s["name"],
        "version": "0.1.0",
        "description": s["en"],
        "author": {"name": "nvvdev", "url": f"https://github.com/{ORG}"},
        "homepage": f"https://github.com/{ORG}/{s['name']}",
        "repository": f"https://github.com/{ORG}/{s['name']}",
        "license": "MIT",
        "keywords": ["skill", s["source_repo"]],
    }
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def export(bundles: Path, out: Path) -> list[dict]:
    catalog = json.loads((HERE / "catalog" / "skills.json").read_text(encoding="utf-8"))["skills"]
    ci_dir = HERE / ".github" / "workflows"
    for s in catalog:
        name, bundle = s["name"], bundles / s["source_repo"]
        src = bundle / "skills" / name
        if not (src / "SKILL.md").exists():
            raise SystemExit(f"missing {src}/SKILL.md")
        repo = out / name
        dst = repo / "skills" / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        (repo / ".claude-plugin").mkdir(parents=True, exist_ok=True)
        (repo / ".claude-plugin" / "plugin.json").write_text(plugin_json(s), encoding="utf-8")
        (repo / "README.md").write_text(readme(s, credits_for(name, bundle)), encoding="utf-8")
        for f in ("LICENSE", ".gitignore"):
            shutil.copy2(HERE / f, repo / f)
        (repo / "scripts").mkdir(exist_ok=True)
        shutil.copy2(HERE / "scripts" / "validate_repo.py", repo / "scripts" / "validate_repo.py")
        (repo / ".github" / "workflows").mkdir(parents=True, exist_ok=True)
        shutil.copy2(ci_dir / "ci.yml", repo / ".github" / "workflows" / "ci.yml")
        shutil.copy2(HERE / ".github" / "dependabot.yml", repo / ".github" / "dependabot.yml")
        shutil.copy2(bundles / "dev-workflow" / ".github" / "workflows" / "skill-scan.yml",
                      repo / ".github" / "workflows" / "skill-scan.yml")
    return catalog


def update_marketplace(catalog: list[dict]) -> None:
    path = HERE / ".claude-plugin" / "marketplace.json"
    market = json.loads(path.read_text(encoding="utf-8"))
    names = {s["name"] for s in catalog}
    plugins = [p for p in market["plugins"] if p["name"] not in names]
    for s in catalog:
        plugins.append({
            "name": s["name"],
            "description": s["en"],
            "category": CATEGORY.get(s["source_repo"], "development"),
            "source": {"source": "url", "url": f"https://github.com/{ORG}/{s['name']}.git"},
            "homepage": f"https://github.com/{ORG}/{s['name']}",
        })
    market["plugins"] = plugins
    path.write_text(json.dumps(market, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_index(catalog: list[dict]) -> None:
    path = HERE / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = "\n".join(
        f"| [{s['name']}](https://github.com/{ORG}/{s['name']}) | {s['tagline']} | "
        f"{'a mano' if s['invocation'] == 'manual' else 'sola'} | {s['source_repo']} |"
        for s in catalog
    )
    block = (
        "<!-- skills:start -->\n"
        "| Skill | En una línea | Se activa | Paquete |\n|---|---|---|---|\n"
        f"{rows}\n<!-- skills:end -->"
    )
    text = re.sub(r"<!-- skills:start -->.*?<!-- skills:end -->", block, text, flags=re.S)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundles", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    catalog = export(args.bundles.resolve(), args.out.resolve())
    update_marketplace(catalog)
    update_index(catalog)
    print(f"exported {len(catalog)} skill repos to {args.out}")


if __name__ == "__main__":
    main()
