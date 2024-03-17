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
    
    def reOrder(self):
        # Finding mid-point
        head = self.head
        sp = head
        fp = head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            
        # Reversing second list
        current = sp
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # Merging two lists
        ptr1, ptr2 = self.head, prev
        while ptr1 and ptr2: 
            temp1 = ptr1.next
            temp2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = temp1
            ptr1 = temp1
            ptr2 = temp2
        
    
    # def reOrderList(self):
LL1 = LinkedList()
for i in range(10):
    LL1.append(i+1)
print("display before redordering : ",end="")
LL1.display()
LL1.reOrder()
print("display after redordering : ",end="")
LL1.display()