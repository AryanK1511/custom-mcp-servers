# raspberrypi/app/adapters/raspberrypi_adapter.py

import paramiko
from app.utils.logger import CustomLogger


class RaspberryPiAdapter:
    def __init__(self, ip: str, username: str, password: str):
        self.ip = ip
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            CustomLogger.create_log(
                "info",
                f"Attempting to connect to Raspberry Pi at {self.ip}, username: {self.username}",
            )
            self.ssh_client.connect(
                hostname=self.ip,
                username=self.username,
                password=self.password,
                timeout=10,
            )
            CustomLogger.create_log(
                "info", f"Successfully connected to Raspberry Pi at {self.ip}"
            )
        except Exception as e:
            CustomLogger.create_log(
                "error", f"Failed to connect to Raspberry Pi: {str(e)}"
            )
            raise

    def disconnect(self):
        try:
            self.ssh_client.close()
        except Exception as e:
            CustomLogger.create_log("error", f"Error while disconnecting: {str(e)}")
            raise

    def execute_command(self, command: str) -> tuple[str, str]:
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        return output, error

    def create_file(self, filepath: str) -> None:
        try:
            self.connect()
            CustomLogger.create_log("info", f"Creating file at path: {filepath}")

            command = f"touch {filepath}"
            output, error = self.execute_command(command)

            if error:
                CustomLogger.create_log("error", f"Failed to create file: {error}")
                raise Exception(f"Failed to create file: {error}")

            CustomLogger.create_log("info", f"File created successfully at {filepath}")
        finally:
            self.disconnect()
