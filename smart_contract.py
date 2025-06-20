from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
contract = w3.eth.contract(address="0xYourContract", abi=[...])

def record_consent_on_chain(user_id, fields, expiration):
    tx_hash = contract.functions.recordConsent(user_id, fields, expiration).transact({'from': w3.eth.accounts[0]})
    return tx_hash