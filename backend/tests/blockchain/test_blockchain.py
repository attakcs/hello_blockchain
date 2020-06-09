from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()

    # first item in the chain list should be the genesis block
    assert blockchain.chain[0].hash ==  GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    blockchain.chain[-1] == data