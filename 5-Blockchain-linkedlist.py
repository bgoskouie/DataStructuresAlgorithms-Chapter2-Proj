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

#--------------TIME AND SPACE COMPLEXITY ANALYSES----------
# - Overall
#     - SPACE:  246 + 68 * n  bytes
#     - TIME:     O(1)

# - DETAILS:
#     - Block:
#         - SPACE:  timestamp (50 chars) + data (1uint) + previous_hash (64) + hash (64) = 182 bytes
#         - TIME:   O(1)
#     - BlockChain:
#         - SPACE:  1Block (182) + 1hash (64) + 1dict (64 + 4) * n = 246 + 68 * n bytes
#         - TIME:   O(1)


import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(timestamp + data)

    def calc_hash(self, _string):
        sha = hashlib.sha256()
        hash_str = _string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def __str__(self):
        return f"timestamp: {self.timestamp}, data={self.data}, hash={self.hash}\n"


class BlockChain():
    """A linked-list of Blocks"""
    def __init__(self):
        self.head = None  # is the element in the chain that is added last (not first)
        self.prev_hash = None
        self.d = dict()

    def insert(self, data, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().__str__()
        b = Block(timestamp, data, self.prev_hash)
        if b.get_hash() not in self.d.keys():
            self.prev_hash = b.get_hash()
            self.head = b
            self.d.update({self.prev_hash: b})
        else:
            print(f"Not adding this data to the blockchain as it already exists under same timestamp \"{timestamp}\" and data \"{data}\".")

    def getByHash(self, hash):
        if hash in self.d:
            return self.d[hash]
        else:
            return None

    def __str__(self):
        b = self.head
        s = ""
        if b is None:
            return "Blockchain is empty!"
        while b.previous_hash is not None:
            s = str(b) + s
            b = self.d[b.previous_hash]
        s = str(b) + s
        s = "Blockchain blocks are as follows:\n" + s
        return s

if __name__ == "__main__":
    print("--------------------Starting Test 1--------------------")
    bc = BlockChain()
    bc.insert("my first sentence")
    bc.insert("Here's a second sentence. Have two now!")
    bc.insert("A third sentence is now being added to the block-chain")
    b = bc.getByHash("HashThatDoesN'tExist")
    print(b)
    print(bc)
    print("--------------------Starting Test 2--------------------")
    bc2 = BlockChain()
    print(bc2)
    print("--------------------Starting Test 3--------------------")
    bc3 = BlockChain()
    timestamp = datetime.now().__str__()
    bc3.insert("my first sentence", timestamp=timestamp)
    bc3.insert("Here's a second sentence. Have two now!", timestamp=timestamp)
    bc3.insert("A third sentence is now being added to the block-chain", timestamp=timestamp)
    print(bc3)  # note that the printed hashes are different!
    print("--------------------Starting Test 4--------------------")
    bc4 = BlockChain()
    timestamp = datetime.now().__str__()
    bc4.insert("my first sentence", timestamp=timestamp)
    bc4.insert("second sentence", timestamp=timestamp)
    bc4.insert("second sentence", timestamp=timestamp)  # timestamp and data the same
    print(bc4)  # note that the printed hashes are different!

