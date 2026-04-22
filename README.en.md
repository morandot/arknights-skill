# Arknights Skill

[中文](./README.md)

An Agent Skill for **Arknights** that helps answer operator evaluation, skill priority, progression planning, lore questions, terminology, and stage strategy.

This repository is intended for public distribution on GitHub and follows the standard Agent Skills directory layout. It is compatible with Codex, the general `skills` CLI, Claude Code, and other clients that support `SKILL.md`-based skill folders.

> Unofficial project.  
> This skill does not bundle a live game database and must not present stale knowledge as current data. For questions about the current meta, latest events, or latest balance state, it should browse first when network access is available; otherwise it must explicitly say the answer is not based on the latest information.

## What This Skill Does

`arknights-skill` is designed to turn Arknights questions into clear, decision-oriented answers rather than dumping raw information.

It mainly covers:

- Operator reviews: role, strengths, weaknesses, and use cases
- Skill priority: recommended skill, mastery order, and tradeoffs
- Progression advice: whether to raise, who to raise first, and efficient investment levels
- Team and stage help: map pressure points, deployment ideas, and low-rarity substitutions
- Lore and story: low-spoiler summaries, relationship context, and spoiler levels
- Terminology: common community terms and their practical meaning
- Version-sensitive questions: explicitly separating fresh, browsed conclusions from non-current judgments

## Typical Use Cases

- “Is this operator worth building?”
- “Which skill should I mastery first?”
- “I’m a new player with limited resources. Who should I build first?”
- “How do I clear this stage? Any low-end substitutes?”
- “What is this character’s backstory? Keep spoilers light.”
- “What do terms like warm-up, cycle, or tech card mean?”
- “Is this operator still strong in the current version?”

## Answer Style

- Lead with the conclusion, then explain why
- Separate objective mechanics from subjective meta evaluation
- Default to low spoilers unless the user asks for more
- Make strategy answers actionable
- Do not invent numbers, event dates, banners, or official text
- Make freshness explicit for version-sensitive conclusions

See [arknights-skill/SKILL.md](./arknights-skill/SKILL.md) for the full instruction set.

## Compatibility

This repository uses the standard Agent Skills layout, with the actual skill located in [`arknights-skill/`](./arknights-skill).

Supported usage patterns:

- Agent Skills / `skills` CLI
- Codex
- Claude Code
- Other clients that support `SKILL.md`-based skill directories

## Installation

### General Method: Ask Your Agent To Install It

If your agent supports the `skills` ecosystem, you can often just send it this message:

```text
Install the skill `arknights-skill` from https://github.com/morandot/arknights-skill
```

If you use Claude Code, you can also say:

```text
Please install this skill for me: https://github.com/morandot/arknights-skill . The skill name is arknights-skill.
```

Many Agent Skills-compatible clients can choose the appropriate install flow automatically. If your client does not, use one of the explicit installation methods below.

### Option 1: Generic `skills` CLI

```bash
npx skills add https://github.com/morandot/arknights-skill --skill arknights-skill
```

Explicit invocation:

```text
$arknights-skill
```

### Option 2: Manual install for Codex

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/arknights-skill" ~/.codex/skills/arknights-skill
```

### Option 3: Manual install for Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)/arknights-skill" ~/.claude/skills/arknights-skill
```

Explicit invocation in Claude Code:

```text
/arknights-skill
```

### Option 4: Hermes-compatible install

```bash
curl -fsSL https://raw.githubusercontent.com/morandot/arknights-skill/main/install.sh | bash
```

Default install path:

```text
~/.hermes/skills/research/arknights-skill
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
- `agents/openai.yaml`: UI/discovery metadata
- `install.sh` / `update.sh`: Hermes compatibility path
- `registry.yaml`: Hermes registry metadata

## Scope Boundaries

This skill does not:

- bundle live scraping scripts
- depend on a third-party game database
- guarantee offline “current version” judgments are up to date
- replace full calculators, database sites, or wikis

It is best used as a structured decision-support skill, not as a live wiki mirror.

## Publishing Notes

- For `skills.sh`: there is no separate submission process. A public, installable repository is enough for discovery through install telemetry. [Reference](https://skills.sh/docs/faq)
- For Claude Code: `arknights-skill/` can be used directly as `.claude/skills/<name>/`. [Reference](https://code.claude.com/docs/en/skills)
- For ClawHub: publishing must follow ClawHub’s versioning and publish flow. Published versions on ClawHub are distributed under ClawHub’s platform rules. [Reference](https://github.com/openclaw/clawhub/blob/main/docs/cli.md)

## Development and Validation

```bash
python3 scripts/quick_validate.py arknights-skill
bash -n install.sh
bash -n update.sh
```

## License

Repository source and docs are licensed under [MIT](./LICENSE).
