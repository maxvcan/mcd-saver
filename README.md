# 麦麦省钱助手（McSaver）

> 一键领券 · 智能比价 · 算出最省点餐方案，还能顺手看看这个月麦当劳有啥活动、积分怎么花最值。
>
> 一个基于 **麦当劳中国 MCP（mcd-mcp）** 的 WorkBuddy Skill，参加「2026 麦当劳程序员创意开发大赛」。

---

## ✨ 它能帮你做什么

| 场景 | 一句话 | 用到的主要 MCP 工具 |
| --- | --- | --- |
| 领券 | "帮我领一下麦麦省的券" | `auto-bind-coupons` / `query-my-coupons` / `available-coupons` / `query-store-coupons` |
| 点最省的 | "帮我点一单最便宜的" | `query-nearby-stores` / `query-meals` / `query-meal-detail` / `calculate-price` / `create-order` |
| 看活动 | "这个月麦当劳有啥活动" | `campaign-calendar` |
| 花积分 | "我的积分怎么花最值" | `query-my-account` / `mall-points-products` / `query-lottery-info` / `draw-lottery` |

核心价值：**不是帮你点多，而是帮你能省则省**——自动领券、跨券比价、算出实付最低的组合，下单前先把账算明白。

---

## 🎯 目标用户

- 常吃麦当劳、想省钱的学生党 / 上班族
- 想用自然语言点餐、不愿研究券面规则的人
- 想顺手蹲限时活动、把积分花在刀刃上的"麦门信徒"

---

## 📦 安装方法（WorkBuddy）

### 1. 申请麦当劳 MCP Token
打开 [https://open.mcd.cn/mcp](https://open.mcd.cn/mcp)，用手机号登录 → 进入「控制台」→ 激活并复制你的 MCP Token。

### 2. 在 WorkBuddy 接入 mcd-mcp
把下面配置写入 WorkBuddy 的 MCP 配置（将 Token 放进环境变量，不要硬编码）：

```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer ${MCD_MCP_TOKEN}"
      }
    }
  }
}
```
> 完整字段见仓库内 `mcp-config.example.json`。

### 3. 安装本 Skill
将本仓库的 `SKILL.md` 放入 WorkBuddy 的 Skills 目录（项目级 `./.workbuddy/skills/mcd-saver/` 或用户级 `~/.workbuddy/skills/mcd-saver/`），重启/重载 Skill 即可。

---

## 🧪 使用示例

```
用户：帮我领一下麦麦省现在能领的券
助手：已一键领取 ✅，加上你账户里已有的，目前可用券共 6 张：
  • 满30减8（全场，10/31到期）
  • 麦辣鸡腿堡买一赠一（限到店，11/05到期）
  • 配送费立减5（麦乐送）
  …

用户：那帮我在公司附近点一单最省的，要一个套餐
助手：附近可配送门店：xx路店。菜单已拉取，结合你手上的券试算了 3 种组合：
  组合A 原价38 → 用满30减8 → 实付30（省8）
  组合B 原价38 → 无合适券 → 实付38
  组合C 原价45 → 买一赠一 → 实付45得两份
推荐组合A。确认我就下单？
用户：确认
助手：已下单 ✅ 订单号 #xxxx，支付链接：https://…
```

---

## 🗂 仓库结构

```
mcd-saver/
├── README.md                 # 本文件：项目介绍 / 安装 / 示例 / 目标用户
├── SKILL.md                  # 核心：WorkBuddy Skill 定义（工作流 + 红线）
├── CONTEST_DECLARATION.md    # 参赛声明（原创性 / 合规 / 敏感信息）
├── MCP_INTEGRATION.md        # MCP Server、Tool、调用流程与业务价值
├── mcp-config.example.json   # 脱敏后的 MCP 配置示例（仅环境变量占位符）
├── workbuddy.md              # WorkBuddy 开发对话上下文（专项奖材料）
├── references/
│   └── tools-reference.md    # mcd-mcp 全部 35 个 Tool 速查
└── scripts/
    └── mcp_client.py         # 使用官方 mcp SDK 直连 MCP 的演示脚本
```

---

## 📄 许可与合规

- 本项目仅以非商业用途使用麦当劳 MCP SDK/示例配置，遵守《麦当劳 MCP 服务规则》。
- 不用于商业售卖、付费分发或任何暗示官方背书的行为。
- 详情见 `CONTEST_DECLARATION.md` 与 `MCP_INTEGRATION.md`。

---

🍔 这个 1024，让代码帮你把每一分钱花在刀刃上。
