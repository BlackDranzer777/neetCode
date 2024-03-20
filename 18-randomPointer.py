# from typing import Optional

# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {None : None}
        current = head

        while current:
            new = Node(current.val)
            hashMap[current] = new
            current = current.next

        current = head
        while current:
            new = hashMap[current]
            new.next = hashMap[current.next]
            new.random = hashMap[current.random]
            current = current.next

        return hashMap[head]
    