# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

_Nothing yet._

## [1.7.0] - 2026-09-02

### Changed
- SKILL.md: `description` now discloses local Doctor profile persistence (storage path, local-only)
- SKILL.md: post-answer profile update is conditional on facts explicitly provided in the current turn
- agents/openai.yaml: greeting no longer recites profile contents; profile is used silently per "Do Not Do These"
- SKILL.md: frontmatter restricted to spec fields (`slug`/`displayName`/`summary` removed, `version` moved into `metadata`); passes the official `skills-ref` validator

### Documentation
- README.md / README.zh-CN.md / references/quickstart.md: added a review-before-run alternative and `REPO_REF` version pinning for the shell installer

## [1.5.0] - 2026-07-28

### Added
- SKILL.md: HARD-GATE (must read profile before answering) and Post-answer gate (must update profile after answering)
- SKILL.md: `license: MIT` frontmatter field
- SKILL.md: "When NOT To Use" section with 4 exclusion scenarios
- SKILL.md: "Common Pitfalls" section with 6 anti-patterns
- references/examples.md: Example 7 "Common Mistakes" with 4 anti-pattern examples (absolute evaluation, squad copy without substitution, old-version caveat, profile dump)
- references/doctor-profile-schema.md: "Edge Cases" section (multi-account, multilingual names, concurrent writes)

### Changed
- SKILL.md: `description` field rewritten with "Use when" trigger keywords upfront and "Do NOT use" gate
- SKILL.md: Rule 3 converted to numbered 4-step checklist with branching
- SKILL.md: Spoiler warning formatted as blockquote
- SKILL.md: "Do Not Do These" expanded (don't recommend pull without roster check, don't dump full profile)
- README.md / README.zh-CN.md: Added badges, "What You Can Ask" table, corrected project structure tree
- references/answer-templates.md: Added M1→M3 value and "most efficient stopping point" fields
- agents/openai.yaml: Workflow steps aligned with HARD-GATE + post-answer gate

## [1.4.0] - 2026-06-05

### Added
- `memory.py list` command: list recorded operators with `--owned` and `--has-pending` filters
- `memory.py search <keyword>` command: search operators by name or notes (case-insensitive)
- `memory.py delete-operator <name>` command: delete a recorded operator from the profile
- `memory.py gc` command: remove stale pending confirmations older than N days (`--days 30`), with `--dry-run` support
- `memory.py update --dry-run` flag: preview merged result without saving
- SKILL.md "Comparison" answer shape for side-by-side operator analysis
- SKILL.md Rule 3 now includes search keyword templates and preferred community sources
- SKILL.md "When To Use" section now includes bilingual example questions per category
- SKILL.md `allowed-tools: shell` frontmatter declaration
- `references/quickstart.md`: step-by-step setup guide
- `references/answer-templates.md`: Comparison template (§7)
- `references/examples.md`: Operator Comparison example (Example 6)
- `agents/openai.yaml`: expanded with `instructions`, `suggested_prompts`, and workflow-oriented `default_prompt`
- `Makefile`: `test`, `lint`, `validate`, `bump`, `dist`, `all`, `clean` targets
- `scripts/build_dist.sh`: automated zip + sha256 dist builder
- `.github/workflows/release.yml`: tag-triggered GitHub Release automation
- README multi-platform install instructions (Hermes, Claude Code, Codex/OpenClaw, Shell)

### Changed
- SKILL.md Rule 0: unified `$SKILL_DIR` fallback chain (single snippet replaces platform-specific blocks)
- SKILL.md Rule 0: new CLI commands documented (list, search, delete-operator, gc, --dry-run)
- `references/doctor-profile-schema.md`: `modules` field corrected from `true/false` to `0–3` stage integers
- `references/doctor-profile-schema.md`: added CLI Commands Reference table
- `.codex/environments/environment.toml`: added `[setup]` script and `[env]` section
- `registry.yaml`: added `en` tag
- CI (`validate.yml`): added `build_dist.sh` syntax check and `quickstart.md`/`doctor-profile-schema.md` to required files

## [1.3.0] - 2026-04-28

### Changed
- **Breaking**: 博士档案默认存储路径从 `<skill-install>/.arknights-memory/` 改为 `~/.config/arknights-skill/doctor-profile.json`，与 skill 安装目录解耦
- 首次运行时自动迁移旧路径数据到新路径（仅当新路径不存在时；旧数据保留不动）
- `merge_mapping_latest` 对数值型字段（`account.progress`、`account.resources`）改为单调递增合并策略，拒绝降级并写入 `pending_confirmations`（原为直接覆盖）

### Added
- `confirm --field <field> --apply` 命令：应用待确认的降级/冲突值
- `dismiss --field <field>` 命令：丢弃待确认项
- `read` 命令输出后在 stderr 显示待确认项摘要
- `scripts/bump_version.sh`：自动同步 VERSION 到 registry.yaml
- `pyproject.toml`：ruff + pytest 配置
- `tests/`：memory.py 全覆盖单元测试
- CI 增加 ruff lint、pytest、必要文件存在性检查
- `update.sh` 支持 `--force` 标志；检测到本地修改时显示 diff

### Removed
- `install.sh` 和 `update.sh` 中对 `.arknights-memory` 的排除逻辑（数据已迁移至 `~/.config/`）

## [1.2.0] - 2026-04-24

### Added
- 新增本地结构化博士档案工作流，支持读取和维护安装目录旁的 `.arknights-memory/doctor-profile.json`
- 新增 `scripts/memory.py`，提供 `path`、`read`、`update --patch-json` 命令，用于初始化、读取和保守合并账号事实

### Changed
- `install.sh` 与 `update.sh` 现在会保留 `.arknights-memory/`，避免更新 skill 时删除本地账号档案
- 更新中英文 README、registry 与 skill metadata，说明本地账号记忆的边界

## [1.1.2] - 2026-04-22

### Changed
- 修复 `install.sh` 与 `update.sh` 的默认仓库 URL，改为 `morandot/arknights-skill`
- 为 `update.sh` 增加 `rsync` 依赖检查，缺失时给出明确报错
- 在 GitHub Actions 中加入 `bash -n install.sh` 与 `bash -n update.sh`
- 丰富 `references/examples.md`，新增“技能选择”和“剧情介绍”示例
- 补充历史命名说明，明确 `arknights-guide` 已在 `1.1.1` 重命名为 `arknights-skill`

## [1.1.1] - 2026-04-22

### Changed
- 将 skill slug、目录名、安装路径和调用方式从 `arknights-guide` 统一为 `arknights-skill`
- 同步更新中英文 README、registry、脚本默认值与验证路径

## [1.1.0] - 2026-04-22

注：本版本中的 `arknights-guide` 目录名和 slug 已在 `1.1.1` 重命名为 `arknights-skill`。

### Added
- 拆分出 `arknights-guide/` 作为独立 skill 包
- 新增 `agents/openai.yaml`
- 新增 `references/answer-templates.md`
- 新增 `references/examples.md`
- 新增 MIT `LICENSE`
- 新增 GitHub Actions 校验工作流

### Changed
- `SKILL.md` 改为合法 YAML frontmatter，并将 slug 统一为 `arknights-guide`
- 精简主 skill 文档，保留核心规则并把长模板移入 `references/`
- 重写 README，明确 Codex 主标准与 Hermes 兼容安装方式
- 重写安装与更新脚本，移除破坏性的 `git reset --hard`
- `registry.yaml` 改为指向真实仓库和 skill 子目录

## [1.0.0] - 2026-04-22

### Added
- 初始版明日方舟攻略 skill
