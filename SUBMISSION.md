# 参赛指南（SUBMISSION.md）

把本仓库推到你的 GitHub 公开仓库，并用官方 Issue 模板报名即可参赛。

## 一、准备麦当劳 MCP Token
1. 打开 https://open.mcd.cn/mcp ，手机号登录。
2. 进入「控制台」→ 激活并复制你的 MCP Token。
3. 本地测试时：`export MCD_MCP_TOKEN="你的Token"`（**不要**写进任何文件）。

## 二、本地安装与自测（可选）
```bash
pip install mcp
export MCD_MCP_TOKEN="你的Token"
python scripts/mcp_client.py      # 验证能连上 mcd-mcp 并列出 Tool
```
在 WorkBuddy 中接入 `mcd-mcp`（见 README「安装方法」），把 `SKILL.md` 放进 Skills 目录即可对话使用。

## 三、推送到 GitHub 公开仓库
```bash
cd mcd-saver
git init
git add .
git commit -m "feat: 麦麦省钱助手 McSaver - 基于麦当劳 MCP 的省钱点餐 Skill"
# 在 GitHub 新建一个 PUBLIC 仓库（如 mcd-saver），然后：
git remote add origin git@github.com:<你的用户名>/mcd-saver.git
git branch -M main
git push -u origin main
```

## 四、用 Issue 模板报名（2026-10-25 23:59 前）
前往 https://github.com/M-China/mcd-developer-innovation-challenge 的 Issues，用官方模板提交：

```
【参赛申请】
项目名称：麦麦省钱助手（McSaver）
项目地址：https://github.com/<你的用户名>/mcd-saver
项目简介：基于麦当劳 MCP 的省钱点餐助手——一键领券、跨券比价算最省、智能下单，附活动日历与积分玩法建议；用 WorkBuddy 开发，参与专项奖。
```

## 五、冲榜要点（排名只看 Star）
- 仓库简介写清楚「能帮人省多少钱」，吸引普通用户收藏。
- 在 README 放一个直观的"省 X 元"演示动图/截图（如有条件）。
- 赛期内（截至 2026-10-26 00:00）分享给朋友/社群求 Star；同一 GitHub 账号多项目只取 Star 最高者进榜，建议只主推这一个。
- 确保仓库始终公开可访问，且 5 个必需文件齐全、命名正确。

## 六、奖励速览
- TOP3：巨无霸免费兑换券（50/30/20 次）+ WorkBuddy 10240 积分
- 进榜前 100：程序员节实体徽章 + 汉堡回车键
- 用 WorkBuddy 开发并交 workbuddy.md：额外 3000 积分
