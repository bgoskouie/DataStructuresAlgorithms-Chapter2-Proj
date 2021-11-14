# Union and Intersection of Two Linked Lists
# Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

# You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

# We have provided a code template below, you are not required to use it:

#--------------TIME AND SPACE COMPLEXITY ANALYSES----------
# union:
#           SPACE:    1LinkedList (4n) + 1dict (4 + 1)n = 9n
#           TIME:     O(n ** 2)
#
# intersection:
#           SPACE:    1LinkedList (4n) + 2dict (4 + 1)n = 14n
#           TIME:     O(n)
#
# DETAILS:
# Node:
#       SPACE:  2 * sizeof(uint)
#       TIME:   O(1)
# LinkedList:
#       SPACE:  n * sizeof(uint)
#       TIME:   append: O(n)    size:  O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1, llist_2):
    union_ll = LinkedList()
    union_d = dict()
    n1 = llist_1.head
    while n1 is not None:
        union_d.update({n1.value: True})
        n1 = n1.next
    n2 = llist_2.head
    while n2 is not None:
        union_d.update({n2.value: True})
        n2 = n2.next
    n1 = llist_1.head
    while n1 is not None:
        if union_d[n1.value]:
            union_ll.append(n1.value)
            union_d[n1.value] = False
        n1 = n1.next
    n2 = llist_2.head
    while n2 is not None:
        if union_d[n2.value]:
            union_ll.append(n2.value)
            union_d[n2.value] = False
        n2 = n2.next
    return union_ll


def intersection(llist_1, llist_2):
    inter_ll = LinkedList()
    inter_d = dict()
    added_d = dict()
    n1 = llist_1.head
    while n1 is not None:
        inter_d.update({n1.value: False})
        added_d.update({n1.value: False})
        n1 = n1.next
    n2 = llist_2.head
    while n2 is not None:
        inter_d.update({n2.value: True})
        added_d.update({n2.value: False})
        n2 = n2.next
    n1 = llist_1.head
    while n1 is not None:
        if inter_d[n1.value] and not added_d[n1.value]:
            inter_ll.append(n1.value)
            added_d[n1.value] = True
        n1 = n1.next
    return inter_ll


def test_union(el1, el2, result):
    union = set(el1 + el2)
    n = result.head
    while n is not None:
        if n.value not in union:
            print(f"Failed as {n.value} should be in union. Failure mode 1.")
        n = n.next
    for el in union:
        found = False
        n = result.head
        while n is not None:
            if n.value == el:
                found = True
            n = n.next
        if not found:
            print(f"Failed as {el} should be in union. Failure mode 2.")
    print("union test passed")


def test_inter(el1, el2, result):
    inter = [el for el in el1 if el in el2]
    n = result.head
    while n is not None:
        if n.value not in inter:
            print(f"Failed as {n.value} should be in inter. Failure mode 1.")
            return
        n = n.next
    for el in inter:
        found = False
        n = result.head
        while n is not None:
            if n.value == el:
                found = True
            n = n.next
        if not found:
            print(f"Failed as {el} should be in inter. Failure mode 2.")
            return
    print("inter test passed")


if __name__ == "__main__":
    print("--------------------Starting Test 1--------------------")
    linked_list_11 = LinkedList()
    linked_list_12 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_11.append(i)

    for i in element_2:
        linked_list_12.append(i)
    u = union(linked_list_11,linked_list_12)
    i = intersection(linked_list_11,linked_list_12)
    print(f"union: {u}")
    print(f"intersection: {i}")
    test_union(element_1, element_2, u)
    test_inter(element_1, element_2, i)

    # Test case 2
    print("--------------------Starting Test 2--------------------")
    linked_list_21 = LinkedList()
    linked_list_22 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_21.append(i)

    for i in element_2:
        linked_list_22.append(i)

    u = union(linked_list_21,linked_list_22)
    i = intersection(linked_list_21,linked_list_22)

    print(f"union: {u}")
    print(f"intersection: {i}")
    test_union(element_1, element_2, u)
    test_inter(element_1, element_2, i)

    # Test case 2
    print("--------------------Starting Test 3--------------------")
    linked_list_31 = LinkedList()
    linked_list_32 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_31.append(i)

    for i in element_2:
        linked_list_32.append(i)

    u = union(linked_list_31,linked_list_32)
    i = intersection(linked_list_31,linked_list_32)

    print(f"union: {u}")
    print(f"intersection: {i}")
    test_union(element_1, element_2, u)
    test_inter(element_1, element_2, i)

    print("--------------------Starting Test 4--------------------")
    linked_list_41 = LinkedList()
    linked_list_42 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_41.append(i)

    for i in element_2:
        linked_list_42.append(i)

    u = union(linked_list_41,linked_list_42)
    i = intersection(linked_list_41,linked_list_42)

    print(f"union: {u}")
    print(f"intersection: {i}")
    test_union(element_1, element_2, u)
    test_inter(element_1, element_2, i)