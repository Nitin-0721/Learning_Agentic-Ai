from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """Get the weather location"""
    return f"The weather is sunny"

@mcp.tool()
async def get_temp(city:str)-> str:
    """Get the temperature of a city"""
    return "25 degrees"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")