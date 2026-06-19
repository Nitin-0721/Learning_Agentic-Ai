from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio

load_dotenv()


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "uv",
                "args": [
                    "run",
                    "python",
                    "mathServer.py",
                ],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable-http",
            },
        }
    ) as client:

        tools = await client.get_tools()

        model = ChatGroq(
            model="llama-3.3-70b-versatile"
        )

        agent = create_react_agent(
            model=model,
            tools=tools
        )

        response = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "What is (3+5)*12?"
                    }
                ]
            }
        )

        print(
            "Math response:",
            response["messages"][-1].content
        )


if __name__ == "__main__":
    asyncio.run(main())