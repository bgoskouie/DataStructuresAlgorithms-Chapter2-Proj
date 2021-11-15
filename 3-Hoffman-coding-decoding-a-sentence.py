# Overview - Data Compression
# In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

# A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.

# A. Huffman Encoding
# Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:

# Phase I - Build the Huffman Tree
# A Huffman tree is built in a bottom-up approach.

# First, determine the frequency of each character in the message. In our example, the following table presents the frequency of each character.
# (Unique) Character	Frequency
# A	7
# B	3
# C	7
# D	2
# E	6
# Each row in the table above can be represented as a node having a character, frequency, left child, and right child. In the next step, we will repeatedly require to pop-out the node having the lowest frequency. Therefore, build and sort a list of nodes in the order lowest to highest frequencies. Remember that a list preserves the order of elements in which they are appended.

# We would need our list to work as a priority queue, where a node that has lower frequency should have a higher priority to be popped-out. The following snapshot will help you visualize the example considered above:


# Can you come up with other data structures to create a priority queue? How about using a min-heap instead of a list? You are free to choose from anyone.

# Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
# Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue.

# Do you think that this reinsertion requires the sorting of priority queue again? If yes, then a min-heap could be a better choice due to the lower complexity of sorting the elements, every time there is an insertion.

# Repeat steps #3 and #4 until there is a single element left in the priority queue. The snapshots below present the building of a Huffman tree.


# For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child. See the final Huffman tree for our example:

# Phase II - Generate the Encoded Data
# Based on the Huffman tree, generate unique binary code for each character of our string message. For this purpose, you'd have to traverse the path from root to the leaf node.
# (Unique) Character	Frequency	Huffman Code
# D	2	000
# B	3	001
# E	6	01
# A	7	10
# C	7	11
# Points to Notice

# Notice that the whole code for any character is not a prefix of any other code. Hence, the Huffman code is called a Prefix code.
# Notice that the binary code is shorter for the more frequent character, and vice-versa.
# The Huffman code is generated in such a way that the entire string message would now require a much lesser amount of memory in binary form.
# Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.
# This way, our encoded data would be 1010101010101000100100111111111111111000000010101010101

# B. Huffman Decoding
# Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data using the following steps:

# Declare a blank decoded string
# Pick a bit from the encoded data, traversing from left to right.
# Start traversing the Huffman tree from the root.
# If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
# If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
# Repeat steps #2 and #3 until the encoded data is completely traversed.
# You will have to implement the logic for both encoding and decoding in the following template. Also, you will need to create the sizing schemas to present a summary.

#--------------TIME AND SPACE COMPLEXITY ANALYSES----------
# SPACE:    2 * n * sizeof(uint)
# TIME:     hoffman_encoding:   O(n ** 2 / 2)
#           hoffman_decoding:   O(n)

# DETAILS:
# HoffmanNode:
#       SPACE:  2 uints;
#       TIME:   setNext O(1), isPrior O(1)
# PriorityQueue:
#       SPACE:  1 HoffmanNode, 1 uint;
#       TIME:   insert O(n), pop O(1)
# huffmanGetCharactersCodes:
#       SPACE:  sizeof(uint)*(2*n) + n**2/2;
#       TIME:   O(n)
# huffman_encoding:
#       SPACE:  1 PriorityQueue, n HoffmanNodes = ((n + 1) * 2 + 1)* sizeof(uint)  ~ 2n*sizeof(uint)
#       TIME:   O(n ** 2 / 2)
# huffman_decoding:
#       TIME:   O(n)

import sys


class HoffmanNode:
    """Binary Tree Node/ also serves as a Hoffman Tree"""
    def __init__(self, priority, value=None, left=None, right=None):   #, next=None):
        """should have either right/left or value. Not both!"""
        if (right is not None or left is not None) and (value is not None):
            raise Exception(f"incorrect insertion, right={right}, left={left}, value={value}!")
        self.priority = priority
        self.value = value  # the letter
        self.left = left
        self.right = right
        self.next = None   # next

    def setNext(self, next):
        self.next = next

    def isPrior(self, node):
        # Would be nice if we could set the default isPrior method to
        # "self.priority > node.priority" and only for Hoffman (or our application here)
        # would override this function to "self.priority < node.priority"
        # Since priority is in reverse order of frequency
        # I don't know how to do it!
        return self.priority < node.priority

    """
    def getCharactersCodes(self):
        ""Run it on the root node of the Hoffman Tree""
        def recur(characters_codes_d, code_from_root, node):
            if node.left is None and node.right is None:
                # This is a leaf node! Append the data:
                characters_codes_d.update({node.value: code_from_root})
            if node.left is not None:
                recur(characters_codes_d, code_from_root + "0", node.left)
            if node.right is not None:
                recur(characters_codes_d, code_from_root + "1", node.right)
        appended_codes = ""
        code_from_root = ""
        characters_codes_d = dict()
        recur(characters_codes_d, code_from_root, self)
        return characters_codes_d
    """

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.__size = 0

    def insert(self, node):
        """Receives a PriorityNode"""
        if node is None:
            return
        self.__size += 1
        elm = self.head
        last = None
        if elm is None:
            self.head = node
        else:
            while elm is not None and elm.isPrior(node):
                last = elm
                elm = elm.next
            if last is not None:
                last.next = node
            else:
                self.head = node
            node.next = elm

    def pop(self):
        elm = self.head
        if self.head is not None:
            next = self.head.next
            self.head = next
            self.__size -= 1
        return elm

    def size(self):
        return self.__size

def huffmanGetCharactersCodes(head):
    """Run it on the root node of the Hoffman Tree
    head should be of type HoffmanNode"""
    def recur(characters_codes_d, code_from_root, node):
        if node.left is None and node.right is None:
            # This is a leaf node! Append the data:
            characters_codes_d.update({node.value: code_from_root})
        if node.left is not None:
            recur(characters_codes_d, code_from_root + "0", node.left)
        if node.right is not None:
            recur(characters_codes_d, code_from_root + "1", node.right)
    appended_codes = ""
    code_from_root = ""
    characters_codes_d = dict()
    if head is not None:
        recur(characters_codes_d, code_from_root, head)
    return characters_codes_d


def huffman_encoding(string_in):
    chars_freqs = dict()
    for c in string_in:
        if c not in chars_freqs.keys():
            chars_freqs.update({c: 1})
        else:
            chars_freqs[c] += 1
    # sort the elements based on ascending frequency
    # chars_freqs_sorted = sorted(chars_freqs.items(), key=lambda item: item[1])
    pq = PriorityQueue()
    for c, freq in chars_freqs.items():  #chars_freqs_sorted:
        node = HoffmanNode(freq, value=c, left=None, right=None)   #, next=None)
        pq.insert(node)
    while pq.size() > 1:
        if pq.size() == 2:
            a = 0
        n1 = pq.pop()
        n2 = pq.pop()
        node = HoffmanNode(n1.priority + n2.priority, value=None, left=n1, right=n2)   #, next=None)
        pq.insert(node)
    # characters_code_d = pq.head.getCharactersCodes()
    characters_code_d = huffmanGetCharactersCodes(pq.head)
    binary_code = ""
    for c in string_in:
        binary_code += characters_code_d[c]
    return binary_code, pq.head

def huffman_decoding(encoded_binary_data, tree_root):
    decoded_data = ''
    node = tree_root
    if encoded_binary_data == '':
        if node is not None:
            decoded_data = node.value * node.priority
    else:
        for idx, c in enumerate(encoded_binary_data):
            if c == "0":
                node = node.left
            elif c == "1":
                node = node.right
            else:
                raise Exception(f"Nonzero or one encoded data of \"{c}\" is found")
            if node.value is not None:
                decoded_data += node.value
                node = tree_root
    return decoded_data


if __name__ == "__main__":
    codes = {}
    print("--------------------Starting Test 1--------------------")
    a_great_sentence = "The bird is the word"   # "ABBCCCDDDDEEEEE"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data1, tree1 = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data1, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data1))
    decoded_data1 = huffman_decoding(encoded_data1, tree1)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data1)))
    print ("The content of the encoded data is: {}\n".format(decoded_data1))

    print("--------------------Starting Test 2--------------------")
    encoded_data2, tree2 = huffman_encoding("AAAAAAAAAAAAAA")
    decoded_data2 = huffman_decoding(encoded_data2, tree2)
    print(decoded_data2)

    print("--------------------Starting Test 3--------------------")
    encoded_data3, tree3 = huffman_encoding("")
    decoded_data3 = huffman_decoding(encoded_data3, tree3)
    print(decoded_data3)

    print("--------------------Starting Test 4--------------------")
    encoded_data4, tree4 = huffman_encoding("AAAAAAAAAAAAAABBB")
    decoded_data4 = huffman_decoding(encoded_data4, tree4)
    print(decoded_data4)
