# Web3Demo MCP Server

A Model Context Protocol (MCP) server for interacting with the Ethereum Sepolia testnet using [web3.py](https://web3py.readthedocs.io/). This server exposes several blockchain utilities as MCP tools, making it easy to query balances, block info, gas prices, and send transactions from Claude or other MCP clients.

---

## Features

- **Get Balance**: Query the Ether balance of any Ethereum address.
- **Get Block Number**: Fetch the latest block number on Sepolia.
- **Get Gas Price**: Get the current gas price in Gwei.
- **Get Chain ID**: Retrieve the current chain ID.
- **Get Testnet Info**: Get a summary of the current testnet status.
- **Get Faucet Info**: Get links to Sepolia testnet faucets.
- **Send Transaction**: Send Ether from a private key to another address.
- **Greeting Resource**: Get a personalized greeting (demo resource).

---

## Prerequisites

- **Python 3.10+** (recommended to use [pyenv](https://github.com/pyenv/pyenv) or similar)
- **[Alchemy](https://alchemy.com/) or [Infura](https://infura.io/)** Sepolia endpoint (free to sign up)
- **Claude Desktop App** (or other MCP-compatible client)

---

## Setup Instructions

### 1. Clone the repository

```bash
# Clone your fork or this repo
git clone <your-repo-url>
cd ekai/ekai
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install 'mcp[cli]' typer web3 eth-utils
```

### 4. Configure your Ethereum RPC URL

Edit `main.py` or set the environment variable before running:

```bash
export ETHEREUM_RPC_URL="https://eth-sepolia.g.alchemy.com/v2/YOUR-API-KEY"
```
Or use your Infura endpoint.

---

## Register and Run the MCP Server

### 1. Register the server with Claude (one-time)

```bash
mcp install main.py
```

### 2. Run the server (keep this running)

```bash
mcp run main.py
```

---

## Update Claude MCP Config for Correct venv Path

If you encounter `No module named 'web3'` or similar errors, ensure Claude launches your server using your venv's `mcp` binary. Edit your Claude config (e.g., `~/Library/Application Support/Claude/claude_desktop_config.json`) to:

```json
"Web3Demo": {
  "command": "/Users/tusharchandra/workspace/repos/ekai/ekai/.venv/bin/mcp",
  "args": [
    "run",
    "/Users/tusharchandra/workspace/repos/ekai/ekai/main.py"
  ]
}
```

Restart Claude after editing this file.

---

## Example Usage

- **Get Balance**
  - Input: Ethereum address
  - Output: Balance in ETH
- **Send Transaction**
  - Input: Private key, recipient address, amount (ETH)
  - Output: Transaction hash or error
- **Get Block Number / Gas Price / Chain ID / Testnet Info**
  - No input needed
  - Output: Corresponding blockchain info
- **Get Faucet Info**
  - No input needed
  - Output: List of faucet URLs

---

Small experiment with MCP Server and web3.

Thanks for your time! :)