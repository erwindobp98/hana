import os
import time
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from a .env file

# Set up connection to the Base network
RPC_URL = os.getenv("BASE_RPC_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
INTERVAL = int(os.getenv("INTERVAL", 6))  # Time interval in seconds (default: 6 detik)
MAX_TRANSACTIONS = int(os.getenv("MAX_TRANSACTIONS", 1000))  # Max transactions to send
DEPOSIT_AMOUNT = float(os.getenv("DEPOSIT_AMOUNT", 0.00000000001))  # Amount of ETH to deposit

w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract_abi = [  # Update with actual ABI
    {
        "inputs": [],
        "name": "depositETH",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def deposit_to_contract():
    nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
    txn = contract.functions.depositETH().build_transaction({
        'from': WALLET_ADDRESS,
        'value': w3.to_wei(DEPOSIT_AMOUNT, 'ether'),  # Configurable deposit amount
        'gas': 300000,  # Adjust gas limit if needed
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce
    })
    
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)

    try:
        txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
        print(f"Transaction successful with hash: {txn_hash.hex()}")
    except Exception as e:
        print(f"Transaction failed: {str(e)}")

def main():
    completed_transactions = 0
    while completed_transactions < MAX_TRANSACTIONS:
        try:
            deposit_to_contract()
            completed_transactions += 1
            time.sleep(INTERVAL)
        except Exception as e:
            print(f"Error in transaction loop: {str(e)}")
            time.sleep(600)  # Retry delay

if __name__ == "__main__":
    main()
