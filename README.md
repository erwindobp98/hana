# hana
Key Changes
Environment Variables: The private key and wallet address are securely loaded from .env using load_dotenv() for better security.
Retry Mechanism: Added a retry mechanism in deposit_to_contract to handle temporary network connection failures.
Logging: Used the logging library for informative and error logging, which provides timestamps and can be configured for more detailed logs.
Adjustable Interval: Defined interval as a variable to easily modify the transaction frequency.

Make sure to set the environment variables in a .env file:
Salin kode
```shell
PRIVATE_KEY=your_private_key
WALLET_ADDRESS=your_wallet_address
