#!/usr/bin/env python3
"""
麦麦省钱助手 —— 麦当劳 MCP 直连演示脚本

使用官方 mcp Python SDK 连接 mcd-mcp，演示：
  1. 初始化 Session
  2. 列出所有可用 Tool
  3. 调用 now-time-info 获取当前时间

仅用于验证"真实使用麦当劳 MCP 能力"，不依赖 WorkBuddy 也可运行。

安装依赖（已在 mcp 2.3.0 验证通过）：
    pip install "mcp>=2.0"

运行（Token 走环境变量，绝不硬编码）：
    # macOS / Linux
    export MCD_MCP_TOKEN="你的麦当劳MCP Token"
    # Windows PowerShell
    $env:MCD_MCP_TOKEN="你的麦当劳MCP Token"
    python scripts/mcp_client.py
"""

import asyncio
import os

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
import httpx2


MCD_MCP_URL = "https://mcp.mcd.cn"


async def main() -> None:
    token = os.environ.get("MCD_MCP_TOKEN")
    if not token:
        raise SystemExit("缺少环境变量 MCD_MCP_TOKEN，请先 export 你的麦当劳 MCP Token。")

    headers = {"Authorization": f"Bearer {token}"}

    async with streamable_http_client(
        MCD_MCP_URL,
        http_client=httpx2.AsyncClient(headers=headers, timeout=30.0),
    ) as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # 1) 列出所有可用 Tool
            tools = await session.list_tools()
            print(f"✅ 已连接 mcd-mcp，可用 Tool 共 {len(tools.tools)} 个：")
            for t in tools.tools:
                print(f"  • {t.name}: {t.description}")

            # 2) 演示调用 now-time-info
            print("\n🕒 调用 now-time-info：")
            result = await session.call_tool("now-time-info", {})
            for item in result.content:
                if getattr(item, "type", None) == "text":
                    print(item.text)


if __name__ == "__main__":
    asyncio.run(main())
