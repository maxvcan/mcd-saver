# MCP 接入说明（MCP_INTEGRATION.md）

## 一、实际使用的麦当劳 MCP Server

| 项 | 值 |
| --- | --- |
| Server 名称 | `mcd-mcp`（麦当劳中国 MCP Server） |
| 官方仓库 | https://github.com/M-China/mcd-mcp-server |
| 开放平台 | https://open.mcd.cn/mcp |
| 接入地址 | `https://mcp.mcd.cn` |
| 传输协议 | Streamable HTTP |
| 鉴权方式 | `Authorization: Bearer <MCP_TOKEN>`（Token 在 open.mcd.cn/mcp 申请） |
| 限流 | 600 次/分钟（超出返回 429） |
| 配置示例 | 见仓库 `mcp-config.example.json` |

本 Skill **真实使用**上述麦当劳 MCP 能力：所有"领券 / 查券 / 点餐 / 算价 / 下单 / 活动 / 积分"功能均通过调用 mcd-mcp 的 Tool 实现，未做本地伪造数据。

## 二、实际使用的 Tool 清单

| Tool | 用途 | 在本 Skill 中的调用场景 |
| --- | --- | --- |
| `now-time-info` | 获取当前时间 | 每次会话起始，用于活动/券有效期判断 |
| `auto-bind-coupons` | 麦麦省一键领券 | 场景 A：批量领取可领券 |
| `available-coupons` | 麦麦省券列表 | 场景 A：列出可领未领券 |
| `query-my-coupons` | 我的优惠券查询 | 场景 A / B：查账户已有券 |
| `query-store-coupons` | 门店可用券 | 场景 A / B：指定门店专属券 |
| `query-nearby-stores` | 附近可用门店 | 场景 B：确定到店/自取门店 |
| `delivery-query-stores` | 可配送门店 | 场景 B：麦乐送选店 |
| `delivery-create-address` | 新增配送地址 | 场景 B：无地址时补全 |
| `query-meals` | 可售餐品列表 | 场景 B：拉菜单 |
| `query-meal-detail` | 餐品详情 | 场景 B：看套餐组成/可替换项 |
| `calculate-price` | 商品价格计算 | 场景 B：逐券试算取最低实付 |
| `create-order` | 创建订单 | 场景 B：用户确认后下单 |
| `campaign-calendar` | 活动日历查询 | 场景 C：当月活动推荐 |
| `query-my-account` | 我的积分查询 | 场景 D：积分余额 |
| `mall-points-products` | 商城商品列表 | 场景 D：可兑换商品 |
| `query-lottery-info` | 抽奖活动信息 | 场景 D：抽奖规则/奖品 |
| `draw-lottery` | 积分抽奖 | 场景 D：用户确认后抽奖（写操作，需确认） |

> 完整 33 个 Tool 速查见 `references/tools-reference.md`。

## 三、典型调用流程（场景 B：点最省的一单）

```
用户意图：在公司附近点一单最省的套餐
   │
   ├─ now-time-info                → 当前时间（用于券有效期）
   ├─ delivery-query-stores        → 附近可配送门店（取第一家）
   ├─ query-meals                  → 该店可售菜单
   ├─ query-meal-detail            → 目标套餐组成
   ├─ auto-bind-coupons            → 先领一波麦麦省券
   ├─ query-store-coupons          → 该店专属券
   ├─ calculate-price              → 商品 + 每张候选券试算
   │     └─ 得到多组 {原价, 优惠, 实付}，取最低
   ├─ [向用户复述方案，等待"确认"]
   └─ create-order                 → 下单，返回支付链接 + 订单号
```

## 四、业务价值

1. **降低决策成本**：用户不必自己研究复杂券面规则，自然语言一句话即可领券、比价、下单。
2. **真实省钱**：通过「跨券试算取最低实付」而非"有券就用"，避免凑单陷阱，最大化优惠。
3. **活动不漏蹲**：结合活动日历主动提示限时优惠，把"被动看到"变"主动提醒"。
4. **合规可控**：所有写操作（下单/抽奖/取消/建地址）均设确认闸门，杜绝误操作与滥用，符合 MCP 服务规则与大赛合规要求。

## 五、与 WorkBuddy 的联动（专项奖）

本 Skill 以 WorkBuddy Skill（SKILL.md）形式交付，直接运行于 WorkBuddy 智能体上下文中，由 WorkBuddy 的 MCP 客户端调用 `mcd-mcp`。完整开发对话上下文见 `workbuddy.md`，满足"真实使用腾讯 WorkBuddy 智能体"的专项奖要求。
