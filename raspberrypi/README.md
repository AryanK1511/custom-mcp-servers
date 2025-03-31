# RaspberryPi MCP Server

This repository sets up a Model Context Protocol (MCP) server that allows the Claude Desktop App to interact with a Raspberry Pi over SSH.

## Running this server locally

### 1. Clone the repository

```bash
git clone git@github.com:<your-github-username>/custom-mcp-servers.git
cd custom-mcp-servers/raspberrypi
```

### 2. Run the server using uv

```bash
uv run -m app.main
```

## Testing with the MCP Inspector

To test the MCP server using the official inspector, run the following command. Replace the path with the absolute path to your `raspberrypi` directory.

```bash
npx @modelcontextprotocol/inspector uv --directory /absolute/path/to/custom-mcp-servers/raspberrypi run -m app.main
```

## Configuring environment variables

Create a `.env` file in the `raspberrypi` directory with the following content:

```env
LOG_LEVEL="INFO"
RASPBERRYPI_IP="<your-raspberry-pi-ip>"
RASPBERRYPI_USERNAME="<your-raspberry-pi-username>"
RASPBERRYPI_PASSWORD="<your-raspberry-pi-password>"
```

These credentials are used to establish an SSH connection to your Raspberry Pi.

## Using this with Claude Desktop App

### 1. Install Claude for Desktop

Download the Claude Desktop App from [here](https://claude.ai/download).

### 2. Modify the MCP server configuration

Open the Claude Desktop configuration file:

```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Add or update the following block. Replace all placeholder paths with the actual ones on your machine:

```json
{
  "mcpServers": {
    "raspberrypi": {
      "command": "/absolute/path/to/uv",
      "args": [
        "--directory",
        "/absolute/path/to/custom-mcp-servers/raspberrypi",
        "run",
        "-m",
        "app.main"
      ]
    }
  }
}
```

Once configured, Claude Desktop will be able to use this MCP server to interact with your Raspberry Pi.

## Author

[Aryan Khurana](https://github.com/AryanK1511)
