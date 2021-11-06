# Blockchain
# https://en.wikipedia.org/wiki/Blockchain
# sha256:  https://en.wikipedia.org/wiki/SHA-2
# Greenwich mean time:   https://en.wikipedia.org/wiki/Greenwich_Mean_Time
# A Blockchain is a sequential chain of records, similar to a linked list.
# Each block contains some information and how it is connected related to the other blocks in the chain.
# Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
# For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

# Use your knowledge of linked lists and hashing to create a blockchain implementation.

# We can break the blockchain down into three main parts.

# First is the information hash:


import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(timestamp + data)

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash


class BlockChain():
    """A linked-list of Blocks"""
    def __init__(self):
        self.tail = None
        self.prev_hash = None
        self.d = dict()

    def insert(self, data):
        now = datetime.now().__str__()
        b = Block(now, data, self.prev_hash)
        self.prev_hash = b.get_hash()
        self.tail = b
        self.d.update({self.prev_hash, data})

    def getByHash(self, hash):
        if hash in self.d:
            return self.d[hash]
        else:
            return None


bc = BlockChain()
bc.insert("my first sentence")
bc.insert("Here's a second sentence. Have two now!")
bc.insert("A third sentence is now being added to the block-chain")
bc.getByHash("HashThatDoesN'tExist")
