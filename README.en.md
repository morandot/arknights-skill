# Arknights Skill

[中文](./README.md)

An Agent Skill for **Arknights** that helps answer operator evaluation, skill priority, progression planning, lore questions, terminology, and stage strategy.

> Unofficial project.  
> It does not bundle a game database and does not replace a live wiki or calculator.
> It can maintain a local structured Doctor profile; it does not save full conversations or upload account data.

## Typical Use Cases

- “Is this operator worth building?”
- “Which skill should I mastery first?”
- “I’m a new player with limited resources. Who should I build first?”
- “How do I clear this stage? Any low-end substitutes?”
- “What is this character’s backstory? Keep spoilers light.”
- “What do terms like warm-up, cycle, or tech card mean?”
- “Is this operator still strong in the current version?”

See [arknights-skill/SKILL.md](./arknights-skill/SKILL.md) for the full instruction set.

## Local Account Memory

After installation, the skill can maintain `.arknights-memory/doctor-profile.json` next to the installed skill directory. It stores structured facts explicitly provided by the user, such as Doctor level, resource priorities, owned operators, and operator investment. Skill updates preserve this directory.

This feature requires the Agent client to support local file access and Python script execution. Without that, the skill still works as a normal guide.

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

To update to the latest version, you can also send this message to your agent:

```text
Update my installed arknights-skill to the latest version from https://github.com/morandot/arknights-skill
```

## License

Repository source and docs are licensed under [MIT](./LICENSE).
