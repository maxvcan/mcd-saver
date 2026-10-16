# 麦当劳 MCP（mcd-mcp）Tool 速查表

> 共 33 个 Tool，来源：https://github.com/M-China/mcd-mcp-server
> 接入：`https://mcp.mcd.cn`，Streamable HTTP，Bearer Token。限流 600 次/分钟。

## 营养 / 菜单 / 门店
| Tool | 说明 |
| --- | --- |
| `list-nutrition-foods` | 餐品营养信息列表（能量/蛋白质/脂肪/碳水/钠/钙等） |
| `query-nearby-stores` | 查询附近可用门店 |
| `query-meals` | 查询当前可售卖的餐品列表（分类/编码/标签） |
| `query-meal-detail` | 查询餐品详情、套餐组成与可替换项 |

## 优惠券
| Tool | 说明 |
| --- | --- |
| `available-coupons` | 麦麦省券列表查询（可领未领） |
| `auto-bind-coupons` | 麦麦省一键领券（无需指定 couponId） |
| `query-my-coupons` | 我的优惠券查询（账户全部可用券） |
| `query-store-coupons` | 用户当前门店下可用的优惠券列表 |

## 麦乐送 / 点餐 / 订单
| Tool | 说明 |
| --- | --- |
| `delivery-query-addresses` | 获取用户可配送地址列表 |
| `delivery-create-address` | 新增配送地址 |
| `delivery-query-stores` | 查询可配送的门店列表 |
| `calculate-price` | 商品价格计算（商品+券→金额/配送费/优惠/应付） |
| `create-order` | 创建订单（返回详情与支付链接） |
| `cancel-order` | 取消订单 |
| `query-order` | 查询订单详情 |
| `order-list` | 查询历史订单（到店/外送） |

## 活动 / 团餐 / 主题
| Tool | 说明 |
| --- | --- |
| `campaign-calendar` | 活动日历查询（当月营销活动） |
| `query-meal-assistance` | 查询助餐服务（企业团餐） |
| `query-party-city` | 主题活动城市列表查询 |
| `query-party-store` | 主题活动门店列表查询 |
| `query-partystore-date` | 主题活动可预约日期查询 |
| `query-partystore-session` | 主题活动可预约日期场次查询 |
| `party-order-create` | 主题活动订单创建 |

## 积分 / 商城 / 抽奖
| Tool | 说明 |
| --- | --- |
| `query-my-account` | 我的积分查询（可用/累计/冻结/即将过期） |
| `mall-points-products` | 查询麦麦商城商品列表（积分/现金） |
| `mall-product-detail` | 查询麦麦商城商品详情 |
| `mall-create-order` | 积分兑换商品下单 |
| `mall-order-list` | 麦麦商城订单查询 |
| `mall-order-detail` | 麦麦商城订单详情查询 |
| `query-lottery-info` | 查看积分抽奖活动信息 |
| `draw-lottery` | 积分抽奖（写操作，需用户确认） |
| `query-my-prizes` | 查看我的奖品 |

## 基础设施
| Tool | 说明 |
| --- | --- |
| `now-time-info` | 获取当前时间信息（建议每次会话起始调用） |

---

### 错误码
- `401`：MCP Token 无效/过期/未提供 → 检查 Authorization 头与 Token。
- `429`：触发限流（>600 次/分钟）→ 降低频率，稍后重试。
