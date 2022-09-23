import hashlib

class Block:
    def __init__(self, index: int, time_span: str, data: str, previous_hash=''):
        self.index = index
        self.time_span = time_span
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    

    def calculate_hash(self) -> str: 
        all_block_data = str(self.index) + self.time_span + self.data + self.previous_hash
        return hashlib.sha256(all_block_data.encode()).hexdigest()
    

    def __str__(self) -> str:
        return 'block hash: ' + self.hash + '\n at index: ' + \
                str(self.index) + ' created at: ' + self.time_span + \
                ' data: ' + self.data + '\n previous hash: ' + self.previous_hash


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    

    def create_genesis_block(self) -> Block:
        return Block(0, "01/01/2022", "Genesis Block", '0')
    

    def get_last_block(self) -> Block:
        return self.chain[-1]
    

    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
    
    def __str__(self):
        chain = ''
        for block in self.chain:
            chain += str(block) + '\n'
        return chain


def main():
    pass


if __name__ == "__main__":
    main()
