# Least Recently Used Cache
# We have briefly discussed caching as part of a practice problem while studying hash maps.

# The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

# While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

# When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

# For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

# Your job is to use an appropriate data structure(s) to implement the cache.

# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.

# Here is some boiler plate code and some example test cases to get you started on this problem:


class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.last = None

class DoublyLinkedList():
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def put(self, key, value):
        newnode = Node(key, value)
        key_to_pop = self.putNode(newnode)
        return key_to_pop

    def putNode(self, newnode):
        """returns the key for the node that may get popped from the queue if it doesn't have space"""
        key_to_pop = None
        if self.capacity == self.size:
            key_to_pop = self.pop()  # pop the tail Node
        if self.head is not None:
            self.head.last = newnode
        newnode.next = self.head
        self.head = newnode
        self.size += 1
        if self.size == 1:
            self.tail = self.head
        return key_to_pop

    def pop(self):
        """removes the tail node of the queue"""
        key_to_pop = None
        # remove tail element
        if self.tail is not None:
            self.size -= 1
            key_to_pop = self.tail.key
            beforetail = self.tail.last
            if beforetail is not None:
                beforetail.next = None
                self.tail = beforetail
            else:  # only one element
                self.tail = None
                self.head = None
        return key_to_pop

    def popNode(self, node):
        """removes any given node from the queue"""
        if node is None:
            return
        nodenext = node.next
        nodelast = node.last
        if nodelast is not None:
            nodelast.next = nodenext
        else: # popping node which is head!
            pass # need to update nodenext first!
        if nodenext is not None:
            nodenext.last = nodelast
        else: # popping node which is tail!
            self.tail = nodelast
        if nodelast is None:  # popping node which is head!
            self.head = nodenext

    def moveNodeToHead(self, node):
        newnode = Node(node.key, node.value)
        self.popNode(node)
        head = self.head
        newnode.last = None
        newnode.next = self.head
        self.head = newnode
        tail = self.tail
        return self.head

    def __repr__(self):
        out = ""
        node = self.head
        out += "doubly linked list contents from head to tail:\n"
        while node is not None:
            out += f"key={node.key}, value={node.value}\n"
            node = node.next
        return out


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.dll = DoublyLinkedList(capacity)
        # to store key -> Node pairs of what is present in the queue
        # so it would give us O(1) access to the Node element
        self.d = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = -1
        if key in self.d:
            node = self.d[key]
            value = node.value
            newnode = self.dll.moveNodeToHead(node)
            self.d.update({key: newnode})
        print(self.dll)
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        new_node = Node(key, value)
        if key not in self.d:
            key_to_pop = self.dll.putNode(new_node)  # always succeeds
            self.d.update({key: new_node})
            if key_to_pop is not None:
                self.d.pop(key_to_pop)
        else:  # key is already in the queue
            # pop it and put it back in again as its value could be different and it should go to the beginning of the queue
            self.dll.popNode(self.d[key])
            self.dll.putNode(new_node)
            # new_node is a pointer so it'd next last attribues should get updated
            self.d.update({key: new_node})
        print(self.dll)

if __name__ == "__main__":
    a = 0

    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    a = our_cache.get(1)       # returns 1
    b = our_cache.get(2)       # returns 2
    c = our_cache.get(9)       # returns -1 because 9 is not present in the cache

    d = our_cache.set(5, 5)
    e = our_cache.set(6, 6)

    f = our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    a = 0
