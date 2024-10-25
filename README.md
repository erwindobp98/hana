Here’s a README.md file to help others set up and run the deposit bot script.
# Ethereum Deposit Bot

This script is an automated bot that deposits a specified amount of ETH into a smart contract's `depositETH` function at regular intervals. The bot is configurable for interval timing, number of transactions, and ETH amount per transaction.

## Requirements

- Python 3.7+
- Node and npm (for managing environment variables with `.env` file)
- An Ethereum wallet with a sufficient balance to cover the transactions
- RPC URL to connect to the Base (or other Ethereum-based) network
- Contract address and ABI for the contract with the `depositETH` function

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/erwindobp98/hana.git
cd hana
```
2. Install Dependencies
Make sure you have web3 and python-dotenv libraries installed. If not, install them using pip:
```bash
pip install web3 python-dotenv
```
3. Set Up Environment Variables
Create a .env file in the project root folder and add the following information:
```bash
BASE_RPC_URL="https://your-rpc-url"
CONTRACT_ADDRESS="0xYourContractAddress"
PRIVATE_KEY="your_private_key_here"
WALLET_ADDRESS="your_wallet_address_here"
INTERVAL=6                 # Time interval in seconds between transactions (default: 6 for 1 detik)
MAX_TRANSACTIONS=1000          # Number of transactions to send
DEPOSIT_AMOUNT=0.00000000001         # ETH amount to deposit per transaction
```
Warning: Make sure to keep the .env file secure as it contains your private key. Do not share this file or include it in public repositories.

4. Run the Script
Once everything is configured, you can run the bot using:
```bash
python bot.py
```
The bot will begin sending transactions based on your settings.
