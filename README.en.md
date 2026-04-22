# Arknights Skill

[中文](./README.md)

An Agent Skill for **Arknights** that helps answer operator evaluation, skill priority, progression planning, lore questions, terminology, and stage strategy.

> Unofficial project.  
> This skill does not bundle a live game database, and it does not replace a live wiki, calculator, or database site. It must not present stale knowledge as current data; for questions about the current meta, latest events, or latest balance state, it should browse first when network access is available, and otherwise explicitly say the answer is not based on the latest information.

## Typical Use Cases

- “Is this operator worth building?”
- “Which skill should I mastery first?”
- “I’m a new player with limited resources. Who should I build first?”
- “How do I clear this stage? Any low-end substitutes?”
- “What is this character’s backstory? Keep spoilers light.”
- “What do terms like warm-up, cycle, or tech card mean?”
- “Is this operator still strong in the current version?”

See [arknights-skill/SKILL.md](./arknights-skill/SKILL.md) for the full instruction set.

## Installation

### Ask Your Agent To Install It

Send this message to your agent:

```text
Install the skill `arknights-skill` from https://github.com/morandot/arknights-skill
```

### Quick Install

```bash
npx skills add https://github.com/morandot/arknights-skill --skill arknights-skill
```

Explicit invocation:

```text
$arknights-skill
```

## Updating

Send this message to your agent:

```text
Update my installed arknights-skill to the latest version from https://github.com/morandot/arknights-skill
```

## Repository Structure

```text
.
├── arknights-skill/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── README.md
├── README.en.md
├── LICENSE
├── CHANGELOG.md
├── install.sh
├── update.sh
└── registry.yaml
```

- `arknights-skill/SKILL.md`: main skill instructions
- `arknights-skill/references/`: templates and style examples
- `arknights-skill/agents/openai.yaml`: UI and discovery metadata
- `install.sh` / `update.sh` / `registry.yaml`: compatibility and distribution support files

## Development and Validation

```bash
python3 scripts/quick_validate.py arknights-skill
bash -n install.sh
bash -n update.sh
```

## License

Repository source and docs are licensed under [MIT](./LICENSE).
