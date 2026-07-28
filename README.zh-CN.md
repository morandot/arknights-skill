# Arknights Skill

[English](./README.md) · [![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-informational)](https://agentskills.io) · [![MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE) · [![Version](https://img.shields.io/badge/version-1.5.0-brightgreen)](./VERSION)

一个面向《明日方舟》的 Agent Skill，用来回答干员定位、技能机制、养成规划、剧情梳理、术语解释和关卡思路——并利用本地博士档案实现个性化建议。

> 非官方项目。
> 不内置游戏数据库，不替代实时 wiki 或计算器。
> 可在本地维护结构化博士档案；不保存完整对话，不上传账号信息。

## 适合什么场景

| 你问 | Skill 做的 |
|------|-----------|
| "这个干员值不值得练？" | 评估定位、优劣、养成优先级 |
| "这个角色一二三技能该专哪个？" | 推荐专精技能和顺序 |
| "我新手资源有限，应该先练谁？" | 根据阵容缺口推荐高效养成路线 |
| "这关怎么打，有没有低配思路？" | 提供可执行的关卡方案 + 替换逻辑 |
| "这个角色的背景故事是什么，先别剧透太多" | 剧透可控的剧情概括 |
| "法蒸、暖机、轴、对策卡是什么意思？" | 清晰定义 + 实战语境 |
| "现在这个干员在当前版本还强吗？" | 实时搜索优先，离线时标注非当前结论 |
| "银灰和棘刺谁更好？" | 按场景分维度对比 |

完整规则见 [arknights-skill/SKILL.md](./arknights-skill/SKILL.md)。

## 本地账号记忆

安装后，skill 可在 `~/.config/arknights-skill/doctor-profile.json` 维护本地博士档案，记录用户明确提供的博士等级、资源倾向、干员拥有与练度等结构化信息。该路径与 skill 安装目录独立，更新或重装 skill 不会影响档案数据。

该能力需要 Agent 客户端支持本地文件访问和 Python 脚本执行；不支持时会退化为普通问答。

## 安装

### 直接让你的 Agent 安装

直接把下面这句话发给你的 agent：

```text
请帮我安装 `arknights-skill`，来源仓库是 https://github.com/morandot/arknights-skill
```

### 各平台安装

**Hermes:**
```bash
skills add git+https://github.com/morandot/arknights-skill.git --skill arknights-skill
```

**Claude Code:**
```text
请帮我安装 `arknights-skill`，来源仓库是 https://github.com/morandot/arknights-skill
```

**Codex / OpenClaw:**
```bash
npx skills add https://github.com/morandot/arknights-skill --skill arknights-skill
```

**手动安装 (Shell):**
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/morandot/arknights-skill/main/install.sh)"
```

显式调用：

```text
$arknights-skill
```

### 更新

更新直接把下面这句话发给你的 agent：

```text
请帮我把已安装的 `arknights-skill` 更新到最新版本，来源仓库是 https://github.com/morandot/arknights-skill
```

或手动执行：

```bash
bash ~/.hermes/skills/research/arknights-skill/update.sh
```

## 快速入门

见 [arknights-skill/references/quickstart.md](./arknights-skill/references/quickstart.md)。

## 项目结构

```
arknights-skill/                  ← repo 根目录
├── arknights-skill/              ← skill 包
│   ├── SKILL.md                  # Skill 指令（frontmatter + 6 条规则 + 7 种回答模板）
│   ├── agents/openai.yaml        # Agent 配置
│   ├── references/
│   │   ├── answer-templates.md   # 7 种回答模板
│   │   ├── examples.md           # 示例节奏（含反模式）
│   │   ├── quickstart.md         # 三步快速入门
│   │   └── doctor-profile-schema.md
│   └── scripts/
│       └── memory.py             # 档案管理工具
├── tests/
│   ├── test_memory.py            # 58 个测试用例
│   └── conftest.py               # 测试夹具
├── CHANGELOG.md                  # 发布历史
├── registry.yaml                 # Hermes 注册
├── pyproject.toml                # Python 项目配置
├── Makefile                      # 构建/测试/格式检查
├── install.sh / update.sh        # 安装/更新脚本
├── VERSION                       # 当前: 1.4.0
├── LICENSE                       # MIT
├── README.md                     # 英文版
└── README.zh-CN.md               # 本文件
```

## License

仓库源码和文档采用 [MIT](./LICENSE)。