# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.1] - 2026-04-22

### Changed
- 将 skill slug、目录名、安装路径和调用方式从 `arknights-guide` 统一为 `arknights-skill`
- 同步更新中英文 README、registry、脚本默认值与验证路径
## [1.1.0] - 2026-04-22

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
