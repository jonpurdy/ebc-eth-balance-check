import ethereum
from pycoin.encoding.hexbytes import b2h, h2b
from web3.auto import w3
#from web3.auto.infura import w3
import random

def main():

    try:
        w3.isConnected()
    except:
        print("Not connected. Exiting.")
        sys.exit()

    iterations = 1000000    # Number of keys we'll try before stopping
    total_found = 0         # Amount of ETH found so far
    wallets_with_eth = []   # List to contain the wallets with ETH
    try_count = 0           # The number of private keys tried so far

    hash = random.getrandbits(256)  # Generate a private key

    try:
        while iterations > 0:

            print("----------")

            private_key = hex(hash)
            print("private_key: %s" % private_key)

            #private_key_example = '89cc3093f4f11d868a61bca31193117681c2955deca1be821067a9e8949841fa'
            
            address = b2h(ethereum.utils.privtoaddr(private_key))

            print("address: 0x%s" % address)

            checksum_address = w3.toChecksumAddress(address)
            balance = w3.fromWei(w3.eth.getBalance(checksum_address), 'ether')

            
            print("balance: %s" % balance)

            if float(balance) > 0:
                wallets_with_eth.append(private_key)
                total_found += balance

            print("Total found: %s ETH  Wallets checked: %s/%s" % (total_found, try_count, iterations))

            hash += 1
            try_count += 1
            iterations -= 1
    except KeyboardInterrupt:
        print("\nFinal stats: %s ETH found." % total_found)
        print("Exiting...")

if __name__ == '__main__':
    main()

