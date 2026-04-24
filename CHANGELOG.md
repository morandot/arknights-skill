# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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
