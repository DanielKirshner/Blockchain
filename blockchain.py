import hashlib


class Block:
    def __init__(self, index: int, time_span: str, data: str, previous_hash=''):
        self.index = index
        self.time_span = time_span
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    

    def calculate_hash(self) -> str: 
        all_block_data = str(self.index) + self.time_span + self.data + self.previous_hash + str(self.nonce)
        return hashlib.sha256(all_block_data.encode()).hexdigest()
    

    def proof_of_work(self, difficulty):
         while self.hash[:difficulty] != ''.zfill(difficulty):
             self.nonce += 1
             self.hash = self.calculate_hash()


    def __str__(self) -> str:
        return 'block hash: ' + self.hash + '\n at index: ' + \
                str(self.index) + ' created at: ' + self.time_span + \
                ' data: ' + self.data + '\n previous hash: ' + self.previous_hash


class BlockChain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
    

    def get_last_block(self) -> Block:
        return self.chain[-1]
    

    def create_genesis_block(self) -> Block:
        return Block(0, "01/01/2022", "Genesis Block", '0')


    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        new_block.proof_of_work(self.difficulty)
        self.chain.append(new_block)
    

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
        if current_block.hash != current_block.calculate_hash() or current_block.previous_hash != previous_block.hash:
            return False
        return True
    
    
    def __str__(self):
        chain = ''
        for block in self.chain:
            chain += str(block) + '\n'
        return chain


def main():
    difficulty = 4
    bitcoin = BlockChain(difficulty)
    bitcoin.add_block(Block(1, '02/01/2022', 'amount = 5'))
    bitcoin.add_block(Block(2, '03/01/2022', 'amount = 15'))
    print(bitcoin)


if __name__ == "__main__":
    main()
