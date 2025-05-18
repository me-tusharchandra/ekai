# main.py
import os
from web3 import Web3
from typing import Optional
from mcp.server.fastmcp import FastMCP
from eth_utils import to_checksum_address

import sys
print("PYTHON EXECUTABLE:", sys.executable, file=sys.stderr)

# Create an MCP server
mcp = FastMCP("Web3Demo")

# Initialize Web3 connection to Sepolia testnet
DEFAULT_SEPOLIA_RPC = "https://eth-sepolia.g.alchemy.com/v2/DhlfOeegZNRhkrvC3E1bLnJ-qN4WqH8g"
w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_RPC_URL', DEFAULT_SEPOLIA_RPC)))

# Verify connection
if not w3.is_connected():
    raise Exception("Failed to connect to Ethereum network")

@mcp.tool()
def get_balance(address: str) -> str:
    """Get the balance of an Ethereum address in Wei"""
    try:
        # Convert address to checksum format
        checksum_address = to_checksum_address(address)
        balance = w3.eth.get_balance(checksum_address)
        # Convert Wei to Ether for better readability
        balance_eth = w3.from_wei(balance, 'ether')
        return f"{balance_eth} ETH"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_block_number() -> int:
    """Get the latest block number"""
    try:
        return w3.eth.block_number
    except Exception as e:
        return -1

@mcp.tool()
def get_gas_price() -> str:
    """Get the current gas price in Gwei"""
    try:
        gas_price = w3.eth.gas_price
        gas_price_gwei = w3.from_wei(gas_price, 'gwei')
        return f"{gas_price_gwei} Gwei"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_chain_id() -> Optional[int]:
    """Get the current chain ID"""
    try:
        return w3.eth.chain_id
    except Exception as e:
        return None

@mcp.tool()
def get_testnet_info() -> dict:
    """Get information about the current testnet"""
    try:
        return {
            "network": "Sepolia Testnet",
            "chain_id": w3.eth.chain_id,
            "block_number": w3.eth.block_number,
            "gas_price": f"{w3.from_wei(w3.eth.gas_price, 'gwei')} Gwei",
            "is_connected": w3.is_connected()
        }
    except Exception as e:
        return {"error": str(e)}

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.tool()
def send_transaction(private_key: str, to_address: str, amount_eth: float) -> str:
    """Send Ether from the private key to the recipient address. Returns the transaction hash or error message."""
    try:
        # Get the account address from the private key
        account = w3.eth.account.from_key(private_key)
        from_address = account.address

        # Convert to checksum address
        to_address = to_checksum_address(to_address)

        # Get the nonce
        nonce = w3.eth.get_transaction_count(from_address)

        # Convert Ether to Wei
        value = w3.to_wei(amount_eth, 'ether')

        # Get current gas price
        gas_price = w3.eth.gas_price

        # Build the transaction
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': value,
            'gas': 21000,
            'gasPrice': gas_price,
            'chainId': w3.eth.chain_id
        }

        # Sign the transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key)

        # Send the transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return f"Transaction sent! Hash: {tx_hash.hex()}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
