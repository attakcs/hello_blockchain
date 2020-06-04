from block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a lift of blocks - data sets of transactions 
    """
    def __init__(self):
      self.chain = []
    # push the instance of the Block in the chain list
    def add_block(self, data):
        self.chain.append(Block(data))
    # returns the object representation
    def __repr__(self):
        return f"Blockchain: {self.chain}"

def main():
    blockchain = Blockchain()
    blockchain.add_block('#1')
    blockchain.add_block('#2')

    print(blockchain)
    print(f"blockchain.py: __name__: {__name__}")
# call main() only when you run this module directly
if __name__ == "__main__":
    main()    
