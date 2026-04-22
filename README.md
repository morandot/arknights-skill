# Arknights Skill

[English](./README.en.md)

一个面向《明日方舟》的 Agent Skill，用来回答干员定位、技能机制、养成规划、剧情梳理、术语解释和关卡思路。

> 非官方项目。  
> 不内置游戏数据库，不替代实时 wiki 或计算器。

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

更新直接把下面这句话发给你的 agent：

```text
请帮我把已安装的 `arknights-skill` 更新到最新版本，来源仓库是 https://github.com/morandot/arknights-skill
```

## License

仓库源码和文档采用 [MIT](./LICENSE)。
