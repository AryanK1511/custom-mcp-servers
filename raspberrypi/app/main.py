# raspberrypi/app/main.py

from app.config import settings
from app.tools.raspberrypi_tool import RaspberryPiTool
from app.utils.logger import CustomLogger
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("raspberrypi")


@mcp.tool()
async def create_file_on_pi(filename: str, path: str, content: str) -> str:
    """
    Create a file on the Raspberry Pi

    * Args:
        * filename (str): The name of the file to create
        * path (str): The path to create the file in.
            * The path will always be relative to the home directory.
            * If no path is provided, the file will be created in the home directory.
        * content (str): The content of the file

    * Returns:
        * str: A success message
    """
    try:
        pi = RaspberryPiTool(
            ip=settings.RASPBERRYPI_IP,
            username=settings.RASPBERRYPI_USERNAME,
            password=settings.RASPBERRYPI_PASSWORD,
        )
        pi.create_file(filename, path, content)

        return f"Successfully created file '{filename}' on Raspberry Pi Desktop."
    except Exception as e:
        return f"Failed to create file: {str(e)}"


@mcp.tool()
async def remove_file_on_pi(file_path: str) -> str:
    """
    Remove a file on the Raspberry Pi

    * Args:
        * file_path (str): The path to the file to remove

    * Returns:
        * str: A success message
    """
    try:
        pi = RaspberryPiTool(
            ip=settings.RASPBERRYPI_IP,
            username=settings.RASPBERRYPI_USERNAME,
            password=settings.RASPBERRYPI_PASSWORD,
        )
        pi.remove_file(file_path)

        return f"Successfully removed file '{file_path}' on Raspberry Pi."
    except Exception as e:
        return f"Failed to remove file: {str(e)}"


if __name__ == "__main__":
    try:
        CustomLogger.create_log("info", "Server initialized successfully")
        mcp.run(transport="stdio")
    except Exception:
        CustomLogger.create_log("critical", "Failed to start MCP server")
        raise
