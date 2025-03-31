# raspberrypi/app/main.py

from app.config import settings
from app.tools.raspberrypi_tool import RaspberryPiTool
from app.utils.logger import CustomLogger
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("raspberrypi")


@mcp.tool()
async def create_file_on_pi(filename: str) -> str:
    """Create a file on the Raspberry Pi's desktop."""
    try:
        pi = RaspberryPiTool(
            ip=settings.RASPBERRYPI_IP,
            username=settings.RASPBERRYPI_USERNAME,
            password=settings.RASPBERRYPI_PASSWORD,
        )
        pi.create_file_on_desktop(filename)

        return f"Successfully created file '{filename}' on Raspberry Pi Desktop."
    except Exception as e:
        return f"Failed to create file: {str(e)}"


if __name__ == "__main__":
    try:
        CustomLogger.create_log("info", "Server initialized successfully")
        mcp.run(transport="stdio")
    except Exception:
        CustomLogger.create_log("critical", "Failed to start MCP server")
        raise
