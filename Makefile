.PHONY: test lint validate bump dist all clean

SKILL_DIR := arknights-skill

test:
	uv run pytest tests/ -v

lint:
	uv run ruff check $(SKILL_DIR)/scripts/memory.py scripts/quick_validate.py tests/

validate:
	uv run python3 scripts/quick_validate.py $(SKILL_DIR)

bump:
	bash scripts/bump_version.sh

dist:
	bash scripts/build_dist.sh

all: lint validate test

clean:
	rm -rf dist/*.zip dist/*.sha256 .pytest_cache .ruff_cache __pycache__ tests/__pycache__
