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
    

    def __str__(self):
        return 'block hash: ' + self.hash + '\n at index: ' + \
                str(self.index) + ' created at: ' + self.time_span + \
                ' data: ' + self.data + '\n previous hash: ' + self.previous_hash


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    

    def create_genesis_block(self):
        return Block(0, "01/01/2022", "Genesis Block", '0')


def main():
    pass


if __name__ == "__main__":
    main()
