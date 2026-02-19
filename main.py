"""
FastMCP Server - Math Tools
Provides two tools:
  1. add_numbers  - adds two numbers together
  2. random_between - returns a random number between two numbers
"""

from fastmcp import FastMCP
import random
import json

# Create the FastMCP server
mcp = FastMCP("Math Tools Server")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


@mcp.tool()
def random_between(min_value: float, max_value: float) -> float:
    """Generate a random number between min_value and max_value (inclusive).

    Args:
        min_value: The minimum value (lower bound)
        max_value: The maximum value (upper bound)

    Returns:
        A random float between min_value and max_value
    """
    if min_value > max_value:
        raise ValueError(
            f"min_value ({min_value}) must be <= max_value ({max_value})")
    return random.uniform(min_value, max_value)


@mcp.resource("info://server")
def tools_info() -> str:
    """Getting information from server"""
    return json.dumps({
        "name": "Math Tools Server",
        "description": "Provides tools for basic math operations",
        "tools": ["add_numbers","random_between"],
    }, indent=2)


if __name__ == "__main__":
    # Run the MCP server using stdio transport (default)
    mcp.run(transport="http", host="0.0.0.0", port=8000)
