# Problem Statement:
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:

# Solution explanation:
I used a Dobuly linked list and a dictionary. The reason is that I wanted the set() and get() operations be of order one.
The dictionary will do a lookup from the item's key to its content (whole node).
Note that after finding the object from the dictionary (hash-map), we have access to the node and then using that we can know where that node in the doubly linked list is located. The dictionary gives us the capability of an O(1) access to the node.
The reason I used a doubly linked list is that, we need to be able to put and pop with O(1). Since we want the Least Recently Used to be removed upon a put, we need quick access to one end of the linked list and since we want to be able to add the new element into the linked list, we need quick access to the other end of the doubly linked list. The Doubly linked list here is the perfect choice as it gives us quick O(1) access to both ends of the linked list.

# Time and Space Analyses:
- Overall
    - SPACE:  `sizeof(uint) * (2*n + 11)`
    - TIME:   All of O(1)

- DETAILS:
    - SPACE:
        - Node class: space 4 uints
        - DoublyLinkedList:  space 2 uints + 2 Nodes = 10 uints
        - LRU_Cache:  1 uint, 1 DoublyLinkedList, 1 dict (2 * n * uint)

    - TIME:
        - moveNodeToHead: O(1)
        - popNode: O(1)
        - pop: O(1)
        - putNode: O(1)