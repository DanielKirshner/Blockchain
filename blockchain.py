class Block:
    def __init__(self, index, time_span, data, previous_hash=''):
        self.index = index
        self.time_span = time_span
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    

    def calculate_hash():
        pass


def main():
    pass


if __name__ == "__main__":
    main()
