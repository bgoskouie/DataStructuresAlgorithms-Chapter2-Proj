# Problem Statement:
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:

# Solution explanation:
To do `union` and `intersection` faster, I created two different dictionaries. Every time, we scrub all the elemnts we fill in the dictionary and as a result, we can find each element much faster a second time by looking up in the dictionary. In these cases, the auxiliary dictionaries help us find if an element is found in both lists or not, so the value of the dictionary is `True` or `False`. 

# Time and Space Analyses:
- union:
    - SPACE:    1LinkedList (4n) + 1dict (4 + 1)n = 9n
    - TIME:     O(n ** 2)

- intersection:
    - SPACE:    1LinkedList (4n) + 2dict (4 + 1)n = 14n
    - TIME:     O(n)

- DETAILS:
    - Node:
        - SPACE:  2 * sizeof(uint)
        - TIME:   O(1)
    - LinkedList:
        - SPACE:  n * sizeof(uint)
        - TIME:   append: O(n)    size:  O(n)