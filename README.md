# Arknights Skill

[English](./README.en.md)

一个面向《明日方舟》的 Agent Skill，用来回答干员定位、技能机制、养成规划、剧情梳理、术语解释和关卡思路。

> 非官方项目。  
> 本 skill 不内置游戏数据库，不替代实时 wiki、计算器或数据库站点，也不会伪装成实时数据源；涉及“当前版本”“最新活动”“最新强度”的问题时，应先联网检索，不能检索时必须明确说明结论不是最新。

## 适合什么场景

- “这个干员值不值得练？”
- “这个角色一二三技能该专哪个？”
- “我新手资源有限，应该先练谁？”
- “这关怎么打，有没有低配思路？”
- “这个角色的背景故事是什么，先别剧透太多”
- “法蒸、暖机、轴、对策卡是什么意思？”
- “现在这个干员在当前版本还强吗？”

完整规则见 [arknights-skill/SKILL.md](./arknights-skill/SKILL.md)。

## 安装

### 直接让你的 Agent 安装

直接把下面这句话发给你的 agent：

```text
请帮我安装 `arknights-skill`，来源仓库是 https://github.com/morandot/arknights-skill
```

### 快速安装

```bash
npx skills add https://github.com/morandot/arknights-skill --skill arknights-skill
```

显式调用：

```text
$arknights-skill
```

## 更新

直接把下面这句话发给你的 agent：

```text
请帮我把已安装的 `arknights-skill` 更新到最新版本，来源仓库是 https://github.com/morandot/arknights-skill
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
- `arknights-skill/agents/openai.yaml`：UI 展示和发现元数据
- `install.sh` / `update.sh` / `registry.yaml`：兼容安装和分发相关文件

## 开发与验证

```bash
python3 scripts/quick_validate.py arknights-skill
bash -n install.sh
bash -n update.sh
```

## License

仓库源码和文档采用 [MIT](./LICENSE)。
