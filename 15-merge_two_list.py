from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = None
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        return
    
    def display(self):
        if self.head is None:
            print("list is empty")
            return
        current = self.head
        while current is not None:
            if current.next is not None:
                print(current.val, end='-->')
            else:
                print(current.val, end='-->Null')
            current = current.next
        print()  # Print a newline after displaying the linked list
        return
    
    def reverseLinkedList(self):
        if self.head == None:
            return print("list is empty")
        current = self.head
        prev = None
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
        


LL1 = LinkedList()
LL1.append(4)
LL1.append(5)
LL1.append(6)
LL1.display()
LL1.reverseLinkedList()
LL1.display()




