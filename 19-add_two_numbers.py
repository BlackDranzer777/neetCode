# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or carry:
            if l1 and l2:
                result = l1.val + l2.val + carry
            elif l1:
                result = l1.val + carry
            elif l2:
                result = l2.val + carry
            else:
                result = carry

            #optimization
            # val1 = l1.val if l1 else 0
            # val2 = l2.val if l2 else 0 
            # result = carry + val1 + val2

            if result > 9:
                carry = result//10
                result = result%10
                cur.next = ListNode(result)
            else:
                carry = result//10
                cur.next = ListNode(result)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next
            