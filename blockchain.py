""" Blockchain """

import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous_block = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        return str(self.timestamp) + ' ' + self.data + ' ' + self.hash + ' ' + str(self.previous_hash)


class Chain:

    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None

    def put(self, block: Block):
        if self.head is None or self.tail is None:
            self.head = block
            self.tail = block
            return
        if block.data is None or block.data == '':
            raise ValueError("block data must not be None or empty")
        if self.head.hash != block.previous_hash:
            raise ValueError("the hash of the previous block doesn't correspond to last block in chain")
        if self.head.timestamp >= block.timestamp:
            raise ValueError("the timestmp of the block must be later than last block in chain")
        block.previous_block = self.head
        self.head = block

    def pop(self):
        if self.head is None or self.tail is None:
            return None
        block = self.head
        self.head = self.head.previous_block
        return block


def test1():
    blockchain = Chain()
    prev_block_hash = None
    for i in range(5):
        block = Block(datetime.datetime.now(), 'I\'m block number ' + str(i), prev_block_hash)
        prev_block_hash = block.hash
        blockchain.put(block)

    cur_block = blockchain.pop()
    while cur_block is not None:
        print(cur_block)
        cur_block = blockchain.pop()


def test2():
    blockchain = Chain()
    try:
        blockchain.put(Block(datetime.datetime.now(), 'I\'m a block', '123'))
        blockchain.put(Block(datetime.datetime.now(), 'I\'m a block', '321'))
    except Exception as e:
        print(str(e))


def test3():
    blockchain = Chain()
    try:
        time1 = datetime.datetime.now()
        time2 = datetime.datetime.now()
        blockchain.put(Block(time2, 'I\'m a block', None))
        blockchain.put(Block(time1, 'I\'m a block', blockchain.head.hash))
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    test1()
    test2()
    test3()
