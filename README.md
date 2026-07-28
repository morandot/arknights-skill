# Arknights Skill

[Chinese](./README.zh-CN.md) · [![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-informational)](https://agentskills.io) · [![MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE) · [![Version](https://img.shields.io/badge/version-1.4.0-brightgreen)](./VERSION)

An Agent Skill for **Arknights** that helps answer operator evaluation, skill priority, progression planning, lore questions, terminology, and stage strategy — personalized using a local Doctor profile.

> Unofficial project.
> It does not bundle a game database and does not replace a live wiki or calculator.
> It can maintain a local structured Doctor profile; it does not save full conversations or upload account data.

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

After installation, the skill maintains a local Doctor profile at `~/.config/arknights-skill/doctor-profile.json`. It stores structured facts explicitly provided by the user, such as Doctor level, resource priorities, owned operators, and operator investment. This path is independent of the skill install directory, so skill updates or reinstalls do not affect profile data.

This feature requires the Agent client to support local file access and Python script execution. Without that, the skill still works as a normal guide.

## Installation

### Ask Your Agent

Send this message to your agent:

```text
Install the skill `arknights-skill` from https://github.com/morandot/arknights-skill
```

### Platform-Specific

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

Explicit invocation:

```text
$arknights-skill
```

### Updating

To update to the latest version, send this message to your agent:

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
arknights-skill/                  ← repo root
├── arknights-skill/              ← skill package
│   ├── SKILL.md                  # Skill instructions (frontmatter + 6 rules + 7 answer shapes)
│   ├── agents/openai.yaml        # Agent configuration
│   ├── references/
│   │   ├── answer-templates.md   # 7 answer templates
│   │   ├── examples.md           # Style examples (inc. anti-patterns)
│   │   ├── quickstart.md         # 3-step setup
│   │   └── doctor-profile-schema.md
│   └── scripts/
│       └── memory.py             # Profile management tool
├── tests/
│   ├── test_memory.py            # 58 test cases
│   └── conftest.py               # Test fixtures
├── CHANGELOG.md                  # Release history
├── registry.yaml                 # Hermes registry
├── pyproject.toml                # Python project config
├── Makefile                      # build/test/lint automation
├── install.sh / update.sh        # Install/update scripts
├── VERSION                       # Current: 1.4.0
├── LICENSE                       # MIT
├── README.md                     # This file (English)
└── README.zh-CN.md               # Chinese version
```

## License

Repository source and docs are licensed under [MIT](./LICENSE).