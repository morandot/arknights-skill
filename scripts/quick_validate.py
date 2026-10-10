#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version
"""

import re
import sys
from pathlib import Path

import yaml

MAX_SKILL_NAME_LENGTH = 64


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as error:
        return False, f"Invalid YAML in frontmatter: {error}"

    allowed_properties = {
        "name",
        "description",
        "license",
        "compatibility",
        "allowed-tools",
        "metadata",
    }

    unexpected_keys = set(frontmatter.keys()) - allowed_properties
    if unexpected_keys:
        allowed = ", ".join(sorted(allowed_properties))
        unexpected = ", ".join(sorted(unexpected_keys))
        return (
            False,
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected}. Allowed properties are: {allowed}",
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # The skill directory name must match the frontmatter name (spec requirement).
    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    if name != skill_path.name:
        return (
            False,
            f"Name '{name}' must match the parent directory name '{skill_path.name}'",
        )

    name = name.strip()
    if name:
        if not re.match(r"^[a-z0-9-]+$", name):
            return (
                False,
                f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)",
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            return (
                False,
                f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens",
            )
        if len(name) > MAX_SKILL_NAME_LENGTH:
            return (
                False,
                f"Name is too long ({len(name)} characters). Maximum is {MAX_SKILL_NAME_LENGTH} characters.",
            )
        if "<" in name or ">" in name:
            return False, "Name cannot contain angle brackets (< or >)"

    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if not description:
        return False, "Description must be non-empty"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets (< or >)"
    if len(description) > 1024:
        return (
            False,
            f"Description is too long ({len(description)} characters). Maximum is 1024 characters.",
        )

    compatibility = frontmatter.get("compatibility", "")
    if compatibility and not isinstance(compatibility, str):
        return False, f"Compatibility must be a string, got {type(compatibility).__name__}"
    if isinstance(compatibility, str) and len(compatibility) > 500:
        return (
            False,
            f"Compatibility is too long ({len(compatibility)} characters). Maximum is 500 characters.",
        )

    metadata = frontmatter.get("metadata")
    if metadata is not None:
        if not isinstance(metadata, dict):
            return False, "Metadata must be a mapping of string keys to string values"
        for key, value in metadata.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False, "Metadata must be a mapping of string keys to string values"

    # Keep SKILL.md body within the progressive-disclosure budget (<500 lines).
    body_lines = content.splitlines()[len(match.group(0).splitlines()) :]
    if len(body_lines) > 500:
        return (
            False,
            f"SKILL.md body is too long ({len(body_lines)} lines). Maximum is 500 lines.",
        )

    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
