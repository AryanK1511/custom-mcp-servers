# raspberrypi/app/tools/raspberrypi_tool.py

from app.adapters.raspberrypi_adapter import RaspberryPiAdapter
from app.utils.logger import CustomLogger


class RaspberryPiTool:
    def __init__(self, ip: str, username: str, password: str):
        self.adapter = RaspberryPiAdapter(ip, username, password)

    def create_file(self, filename: str, path: str, content: str) -> None:
        try:
            self.adapter.connect()
            full_path = f"{path}/{filename}"
            CustomLogger.create_log(
                "debug", f"Creating {filename} at path {path} with content: {content}"
            )

            escaped_content = content.replace('"', '\\"')
            command = f'printf "{escaped_content}" > "{full_path}"'
            output, error = self.adapter.execute_command(command)

            if error:
                CustomLogger.create_log("error", f"Failed to create file: {error}")
                raise Exception(f"Failed to create file: {error}")

            CustomLogger.create_log(
                "info", f"File created successfully at {path}/{filename}"
            )
        finally:
            self.adapter.disconnect()

    def remove_file(self, file_path: str) -> None:
        try:
            self.adapter.connect()
            CustomLogger.create_log("debug", f"Removing file {file_path}")
            command = f"rm -f {file_path}"
            output, error = self.adapter.execute_command(command)

            if error:
                CustomLogger.create_log("error", f"Failed to remove file: {error}")
                raise Exception(f"Failed to remove file: {error}")

            CustomLogger.create_log("info", f"File removed successfully at {file_path}")
        finally:
            self.adapter.disconnect()
