# raspberrypi/app/tools/raspberrypi_tool.py

from app.adapters.raspberrypi_adapter import RaspberryPiAdapter
from app.utils.logger import CustomLogger


class RaspberryPiTool:
    def __init__(self, ip: str, username: str, password: str):
        self.adapter = RaspberryPiAdapter(ip, username, password)

    def create_file_on_desktop(self, filename: str) -> None:
        try:
            desktop_path = f"/home/{self.adapter.username}/Desktop/{filename}"
            self.adapter.create_file(desktop_path)
            CustomLogger.create_log(
                "info", f"File '{filename}' created on Raspberry Pi Desktop."
            )
        except Exception as e:
            CustomLogger.create_log(
                "error", f"Failed to create file on desktop: {str(e)}"
            )
            raise
