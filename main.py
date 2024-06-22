from tronpy import Tron, HttpProvider
from tronpy.keys import PrivateKey
import time

# Configure your private key and endpoint
private_key = PrivateKey(bytes.fromhex('YOUR_PRIVATE_KEY'))
tron = Tron(private_key=private_key, provider=HttpProvider('https://api.trongrid.io'))

# Define your wallet address for auto withdrawal
wallet_address = 'YOUR_WALLET_ADDRESS'

# Define the threshold for auto withdrawal
withdraw_threshold = 1.5  # in Tron

# Function to participate in Tron mining (block production)
def mine_tron():
    account = tron.get_account()
    # Example of voting for a Super Representative
    votes = [{'vote_address': 'Super_Rep_Address', 'vote_count': 1_000_000}]  # Adjust vote count as needed
    tron.vote(votes, account['address'])

# Main loop for monitoring balance and mining
while True:
    try:
        # Check your Tron balance
        balance = tron.get_account_balance()
        tron_balance = balance / 10**6  # Convert from SUN to Tron

        # Check if balance exceeds withdrawal threshold
        if tron_balance >= withdraw_threshold:
            # Withdraw to your wallet
            tx = tron.withdraw(tron_balance, wallet_address)
            print(f"Withdrawal transaction sent: {tx}")

        # Mine Tron through super representatives or other mining process
        mine_tron()

        # Sleep for some time before checking again
        time.sleep(180)  # Check every minute

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(180)  # Wait before retrying
