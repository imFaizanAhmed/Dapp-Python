from eth_utils import address
from web3 import Web3
import json

ganache_url = "HTTP://127.0.0.1:7545"
### url should look like this https://mainnet.infura.io/v3/0917e

web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xb3145eFF8549354Efec30b962d4b90593e547C8d"
account_2 = "0x206c1Acbd7c4d5e01C13B4adf3A6A5F4184a3976"

private_key = "5a431c2000f7dfafc3ad96b1a98aefc211b82088c1ab827611ef2046ea1a0f8e"

# get the nonce
nonce = web3.eth.getTransactionCount(account_1);

# build the transcation
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign the transcation
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send the transcation
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("Transction Hash: ", tx_hash)

# get transcation hash