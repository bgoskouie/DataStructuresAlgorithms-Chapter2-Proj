# Problem Statement:
Blockchain
https://en.wikipedia.org/wiki/Blockchain
sha256:  https://en.wikipedia.org/wiki/SHA-2
Greenwich mean time:   https://en.wikipedia.org/wiki/Greenwich_Mean_Time
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

We can break the blockchain down into three main parts.

First is the information hash:


# Solution explanation:
A BlockChain consists of Blocks each has a hash code (256 bits) = 64 bytes. They are connected like a linked list to each other using their hash 128s. each block has a unique hash that is found from the timestamp of creation of the data and the string data.  Knowing that hashs are distinct, we use a dictionary (hash-map) to look up the Block associated to every hash. So then given every hash, we can fin dthe Block in O(1) because we are using dictionaries.

# Time and Space Analyses:
- Overall
    - SPACE:  246 + 68 * n  bytes
    - TIME:     O(1)

- DETAILS:
    - Block:
        - SPACE:  timestamp (50 chars) + data (1uint) + previous_hash (64) + hash (64) = 182 bytes
        - TIME:   O(1)
    - BlockChain:
        - SPACE:  1Block (182) + 1hash (64) + 1dict (64 + 4) * n = 246 + 68 * n bytes
        - TIME:   O(1)
