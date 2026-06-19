from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers"""
    return a+b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers"""
    return a*b

#the transport = "stdio" argument tells the server to:
#use standard input/output (stdin and stdout) to receive and respond to tool function calls

if __name__ == "__main__":
    mcp.run(transport="stdio")