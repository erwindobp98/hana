import os
import time
import logging
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logging for error tracking
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to center text for UI purposes
def center_text(text):
    terminal_width = os.get_terminal_size().columns
    lines = text.splitlines()
    centered_lines = [line.center(terminal_width) for line in lines]
    return "\n".join(centered_lines)

# Description Text
description = """
HANA NETWORK
BY : PUCUK KANGKUNG KONTOL BABI
- KONTOL NGENTOD ANJING
"""

# Print centered description
print(center_text(description))
print("\n\n")

# Network information (Base)
network = {
    'name': 'Base',
    'rpc_url': 'https://base.llamarpc.com',
    'chain_id': 8453,
    'contract_address': '0xC5bf05cD32a14BFfb705Fb37a9d218895187376c'
}

# Wallet details loaded from environment variables for security
wallet = {
    'private_key': os.getenv("PRIVATE_KEY"),
    'address': os.getenv("WALLET_ADDRESS")
}

# Contract ABI for depositETH
contract_abi = [
    {
        "constant": False,
        "inputs": [],
        "name": "depositETH",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    }
]

# Function to deposit ETH using the depositETH function in the contract
def deposit_to_contract(network, private_key, from_address, amount_in_eth):
    web3 = Web3(Web3.HTTPProvider(network['rpc_url']))
    retries = 3  # Retry up to 3 times if connection fails
    
    for attempt in range(retries):
        if web3.is_connected():
            break
        elif attempt < retries - 1:
            time.sleep(5)  # Wait before retrying
            logging.warning(f"Retrying connection... ({attempt + 1}/{retries})")
        else:
            logging.error(f"Failed to connect to {network['name']} after {retries} attempts.")
            return None

    contract = web3.eth.contract(address=network['contract_address'], abi=contract_abi)
    nonce = web3.eth.get_transaction_count(from_address)

    transaction_value = web3.to_wei(amount_in_eth, 'ether')
    
    try:
        gas_estimate = contract.functions.depositETH().estimate_gas({'from': from_address, 'value': transaction_value})
        gas_limit = gas_estimate + 10000
    except Exception as e:
        logging.error(f"Error estimating gas: {e}")
        return None

    current_gas_price = web3.eth.gas_price
    max_priority_fee_per_gas = int(min(current_gas_price * 0.1, web3.to_wei(0.052, 'gwei')))
    max_fee_per_gas = int(current_gas_price + max_priority_fee_per_gas)

    balance = web3.eth.get_balance(from_address)
    total_cost = transaction_value + (gas_limit * max_fee_per_gas)
    
    if balance < total_cost:
        logging.error(f"Insufficient funds. Balance: {web3.from_wei(balance, 'ether')} ETH, Required: {web3.from_wei(total_cost, 'ether')} ETH")
        return None

    transaction = contract.functions.depositETH().build_transaction({
        'nonce': nonce,
        'value': transaction_value,
        'gas': gas_limit,
        'maxFeePerGas': max_fee_per_gas,
        'maxPriorityFeePerGas': max_priority_fee_per_gas,
        'chainId': network['chain_id'],
    })

    try:
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3.to_hex(tx_hash)
    except Exception as e:
        logging.error(f"Transaction error: {e}")
        return None

def main():
    amount_in_eth = 0.00000000001  # ETH amount to deposit
    interval = 15  # Set time interval (in seconds), here it is 15 detik

    while True:
        start_time = time.time()

        tx_hash = deposit_to_contract(network, wallet['private_key'], wallet['address'], amount_in_eth)

        end_time = time.time()
        duration = end_time - start_time

        if tx_hash:
            logging.info(f"Network: {network['name']} | Tx Hash: {tx_hash}")
        else:
            logging.error("Transaction failed")

        logging.info(f"Transaction execution time: {duration:.2f} seconds")
        
        # Delay before next transaction
        time.sleep(interval)

if __name__ == "__main__":
    main()
