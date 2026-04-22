# Arknights Skill

[English](./README.en.md)

一个面向《明日方舟》的 Agent Skill，用来回答干员定位、技能机制、养成规划、剧情梳理、术语解释和关卡思路。

这个仓库适合公开分发到 GitHub，并兼容主流 Agent Skills 生态，包括 Codex、通用 `skills` CLI、Claude Code，以及需要手动导入 skill 目录的其他客户端。

> 非官方项目。  
> 本 skill 不内置游戏数据库，也不会伪装成实时数据源；涉及“当前版本”“最新活动”“最新强度”的问题时，应先联网检索，不能检索时必须明确说明结论不是最新。

## 这个 Skill 做什么

`arknights-skill` 的目标不是堆资料，而是把《明日方舟》问题整理成玩家可以直接拿来做决定的回答。

主要覆盖：

- 干员简评：定位、强项、短板、适用场景
- 技能选择：推荐技能、专精顺序、替代判断
- 养成建议：值不值得练、先练谁、练到什么程度
- 阵容与关卡：关卡难点、部署思路、低配替代
- 世界观与剧情：低剧透简介、关系梳理、完整剧透分级
- 术语解释：常见社区说法和实战含义
- 版本相关问题：明确区分“最新检索结论”和“非最新判断”

## 适合什么场景

- “这个干员值不值得练？”
- “这个角色一二三技能该专哪个？”
- “我新手资源有限，应该先练谁？”
- “这关怎么打，有没有低配思路？”
- “这个角色的背景故事是什么，先别剧透太多”
- “法蒸、暖机、轴、对策卡是什么意思？”
- “现在这个干员在当前版本还强吗？”

## 回答风格

- 先给结论，再给依据
- 区分客观机制和主观环境评价
- 默认低剧透，按需提升剧透等级
- 攻略必须可执行，不能只说抽象道理
- 不编造数值、活动时间、池子安排或官方文本
- 涉及时效性结论时，必须说明是不是基于最新检索

完整规则见 [arknights-skill/SKILL.md](./arknights-skill/SKILL.md)。

## 兼容性

当前仓库采用标准 Agent Skills 目录结构，skill 本体位于 [`arknights-skill/`](./arknights-skill)。

已对齐的使用方式：

- Agent Skills / `skills` CLI
- Codex
- Claude Code
- 其他支持 `SKILL.md` 目录结构的客户端

## 安装

### 通用方式：直接让你的 Agent 安装

如果你的 agent 支持 `skills` 生态，可以直接把下面这句话发给它：

```text
Install the skill `arknights-skill` from https://github.com/morandot/arknights-skill
```

如果你在用 Claude Code，也可以直接说：

```text
请帮我安装这个 skill：https://github.com/morandot/arknights-skill ，skill 名称是 arknights-skill
```

多数支持 Agent Skills 的客户端会自动选择合适的安装方式；如果不能自动安装，再使用下面的显式命令。

### 方式 1：通用 `skills` CLI

```bash
npx skills add https://github.com/morandot/arknights-skill --skill arknights-skill
```

显式调用：

```text
$arknights-skill
```

### 方式 2：Codex 手动安装

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/arknights-skill" ~/.codex/skills/arknights-skill
```

### 方式 3：Claude Code 手动安装

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)/arknights-skill" ~/.claude/skills/arknights-skill
```

在 Claude Code 中可显式调用：

```text
/arknights-skill
```

### 方式 4：Hermes 兼容安装

```bash
curl -fsSL https://raw.githubusercontent.com/morandot/arknights-skill/main/install.sh | bash
```

默认安装到：

```text
~/.hermes/skills/research/arknights-skill
```

## 仓库结构

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

- `arknights-skill/SKILL.md`：skill 主体说明
- `arknights-skill/references/`：模板和风格示例
- `agents/openai.yaml`：UI 展示和发现元数据
- `install.sh` / `update.sh`：Hermes 兼容链路
- `registry.yaml`：Hermes registry 元数据

## 设计边界

这个 skill 当前不做这些事情：

- 不内置实时抓取脚本
- 不绑定第三方游戏数据源
- 不保证离线状态下的“当前版本”判断是最新的
- 不替代详细配装器、伤害计算器或数据库站点

它更适合做高质量决策辅助和结构化解释，而不是当作实时 wiki 镜像。

## 发布与使用说明

- 对 `skills.sh`：不需要额外提交流程，只要仓库公开、可安装，就可以通过安装遥测自然出现。[参考](https://skills.sh/docs/faq)
- 对 Claude Code：该仓库里的 `arknights-skill/` 可直接作为 `.claude/skills/<name>/` 使用。[参考](https://code.claude.com/docs/en/skills)
- 对 ClawHub：发布时需要按 ClawHub 的发布流程和版本号要求操作；ClawHub 平台发布版本按其平台规则分发。[参考](https://github.com/openclaw/clawhub/blob/main/docs/cli.md)

## 开发与验证

```bash
python3 scripts/quick_validate.py arknights-skill
bash -n install.sh
bash -n update.sh
```

## License

仓库源码和文档采用 [MIT](./LICENSE)。
