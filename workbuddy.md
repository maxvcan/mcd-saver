# WorkBuddy 开发对话上下文（workbuddy.md）

> 本文件记录使用腾讯 WorkBuddy 智能体从 0 到 1 完成「麦麦省钱助手」参赛 Skill 的完整过程，作为 WorkBuddy 专项奖励的提交材料。

---

## 阶段一：需求与赛事规则调研

**用户**：发来公众号推文链接，想参加「2026 麦当劳程序员创意开发大赛」，让我帮他做一个 Skill。

**WorkBuddy 行动**：
1. 用 WebFetch 抓取推文，确认活动主题、时间（2026-10-09 ~ 2026-10-25）、奖励结构。
2. 用 WebSearch 检索到官方规则仓库 `M-China/mcd-developer-innovation-challenge` 与 MCP 仓库 `M-China/mcd-mcp-server`。
3. 用 WebFetch 抓取两份仓库 README / activityGuidelines.md，提炼出关键约束：
   - 排名只看 GitHub 公开 Star 数，前 100 进榜即送实体周边；
   - 必须"真实使用麦当劳 MCP 能力"；
   - WorkBuddy 专项奖要求"真实使用腾讯 WorkBuddy 智能体"并提交本文件；
   - 必交 5 个文件：README.md / CONTEST_DECLARATION.md / MCP_INTEGRATION.md / mcp-config.example.json / workbuddy.md。

**关键决策**：因为排名靠 Star，Skill 必须"真的好用、能涨收藏"，故选受众最广的「省钱助手」方向——领券 + 比价 + 算最省 + 下单，并补齐活动日历与积分玩法。

## 阶段二：摸清 MCP 能力边界

**WorkBuddy 行动**：抓取 `mcd-mcp-server` README，整理出：
- 接入地址 `https://mcp.mcd.cn`，Streamable HTTP + Bearer Token，限流 600 次/分钟；
- 已开放 **33 个 Tool**，覆盖点餐、领券、活动日历、积分抽奖、商城、主题活动等。
- 据此在 `MCP_INTEGRATION.md` 中锁定本 Skill 实际调用的 17 个 Tool。

## 阶段三：设计 Skill 工作流

**WorkBuddy 行动**：把用户意图拆成 4 类场景（领券 / 点最省的 / 看活动 / 花积分），为每类设计"先查时间 → 调工具 → 汇总 → 确认再写操作"的流程，并设定红线：所有下单/抽奖/扣积分等写操作必须先复述方案、等用户确认。这部分沉淀为 `SKILL.md`。

## 阶段四：产出参赛文件

**WorkBuddy 行动**：并行生成全部必需文件：
- `SKILL.md`：核心 Skill 定义（frontmatter + 工作流 + 输出风格 + 红线）；
- `README.md`：项目介绍、安装（申请 Token → 配 MCP → 装 Skill）、使用示例、目标用户；
- `CONTEST_DECLARATION.md`：原创性 / 合规性 / 敏感信息三块声明，明确不含真实 Token、无刷券绕过限流；
- `MCP_INTEGRATION.md`：Server 信息、17 个 Tool 映射表、典型调用流程图、业务价值；
- `mcp-config.example.json`：仅 `${MCD_MCP_TOKEN}` 占位符，无硬编码密钥；
- `references/tools-reference.md`：33 个 Tool 速查；
- `scripts/mcp_client.py`：用官方 `mcp` SDK 直连 MCP 的演示脚本（list_tools + now-time-info 示例）。

## 阶段五：自检与交付

**WorkBuddy 行动**：
- 校验 `mcp-config.example.json` 为合法 JSON；
- 校验 `scripts/mcp_client.py` 语法通过 `python -m py_compile`；
- 在本地 `mcd-saver/` 初始化 git 仓库并提交，生成「GitHub 推送 + Issue 报名」步骤清单交付给用户。

## 本项目的 WorkBuddy 使用特征（专项奖佐证）
- 全程由 WorkBuddy 智能体完成调研、设计、写作、校验与 git 初始化；
- 交付物为可直接在 WorkBuddy 中加载运行的 Skill（SKILL.md）；
- 所有麦当劳 MCP 调用通过 WorkBuddy 的 MCP 客户端发生，符合"真实使用腾讯 WorkBuddy 智能体"。

---

*— 以上为「麦麦省钱助手」在 WorkBuddy 中的完整开发上下文记录。*
