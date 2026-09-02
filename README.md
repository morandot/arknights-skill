# Arknights Skill

[English](./README.md) · [中文](./README.zh-CN.md)

[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-informational)](https://agentskills.io)
[![MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.7.0-brightgreen)](./VERSION)

An Agent Skill for **Arknights** that helps answer operator evaluation, skill priority, progression planning, lore questions, terminology, and stage strategy, personalized with a local Doctor profile.

> Unofficial project.  
> Does not bundle a game database or replace a live wiki or calculator.  
> Maintains a local structured Doctor profile. Does not save full conversations or upload account data.

## What You Can Ask

| You Ask | What The Skill Does |
|---------|-------------------|
| "Is this operator worth building?" | Evaluates role, strengths, weaknesses, investment priority |
| "Which skill should I mastery first?" | Recommends skill priority with mastery order |
| "I'm a new player with limited resources. Who should I build first?" | Suggests efficient build order based on roster gaps |
| "How do I clear this stage? Any low-end substitutes?" | Provides executable stage plan with substitution logic |
| "What is this character's backstory? Keep spoilers light." | Spoiler-controlled lore summary |
| "What do terms like warm-up, cycle, or tech card mean?" | Clear definitions with practical context |
| "Is this operator still strong in the current version?" | Search-first freshness check, or caveated non-current answer |
| "SilverAsh vs Thorns, who is better?" | Side-by-side comparison by scenario |

See [arknights-skill/SKILL.md](./arknights-skill/SKILL.md) for the full instruction set.

## Local Account Memory

After installation, the skill keeps a local Doctor profile at `~/.config/arknights-skill/doctor-profile.json`. It stores structured facts you provide: Doctor level, resource priorities, owned operators, and operator investment. The path is independent of the skill install directory, so updates or reinstalls won't touch your profile data.

This feature requires the Agent client to support local file access and Python script execution. Without that, the skill still works as a normal guide.

## Installation

### Ask your agent

Send this to your agent:

```text
Install the skill `arknights-skill` from https://github.com/morandot/arknights-skill
```

### Platform-specific

**Hermes:**
```bash
skills add git+https://github.com/morandot/arknights-skill.git --skill arknights-skill
```

**Claude Code:**
```text
Install the skill `arknights-skill` from https://github.com/morandot/arknights-skill
```

**Codex / OpenClaw:**
```bash
npx skills add https://github.com/morandot/arknights-skill --skill arknights-skill
```

**Shell (manual):**
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/morandot/arknights-skill/main/install.sh)"
```

This runs a script fetched from GitHub. To review it first:

```bash
curl -fsSL -o /tmp/arknights-install.sh https://raw.githubusercontent.com/morandot/arknights-skill/main/install.sh
less /tmp/arknights-install.sh   # inspect the script
bash /tmp/arknights-install.sh   # run after review
```

To pin a released version instead of `main`, set `REPO_REF` (e.g. `REPO_REF=v1.5.0`).

Once installed, invoke the skill directly in any agent session with:

```text
$arknights-skill
```

### Updating

Send this to your agent:

```text
Update my installed arknights-skill to the latest version from https://github.com/morandot/arknights-skill
```

Or run manually:

```bash
bash ~/.hermes/skills/research/arknights-skill/update.sh
```

## Quick Start

See [arknights-skill/references/quickstart.md](./arknights-skill/references/quickstart.md) for a step-by-step guide.

## Project Structure

```
arknights-skill/
├── arknights-skill/              # skill package
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/
│   │   ├── answer-templates.md
│   │   ├── examples.md
│   │   ├── quickstart.md
│   │   └── doctor-profile-schema.md
│   └── scripts/
│       └── memory.py
├── tests/
│   ├── test_memory.py
│   └── conftest.py
├── CHANGELOG.md
├── registry.yaml
├── pyproject.toml
├── Makefile
├── install.sh
├── update.sh
├── VERSION
├── LICENSE
├── README.md
└── README.zh-CN.md
```

## License

Repository source and docs are licensed under [MIT](./LICENSE).
