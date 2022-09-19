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


def main():
    pass


if __name__ == "__main__":
    main()
