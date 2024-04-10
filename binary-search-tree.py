class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val):
        if self.data == val:
            return
        
        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTreeNode(val)

        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTreeNode(val)
    
    def in_order_traversal(self):
        elements = []

        #visit left nodes first
        if self.left:
            elements+= self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right node
        if self.right:
            elements+= self.right.in_order_traversal()

        return elements
    
    def find_max(self):
        marker = self
        while marker.right:
            marker = marker.right
        return marker.data
    
    def find_min(self):
        marker = self
        while marker.left:
            marker = marker.left
        return marker.data

#Helper Function to create trees

def build_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])
    return root


if __name__ == '__main__':
    elements = [17, 23, 5, 2, 47, 28, 4, 1, 6, 56, 11, 15, -1]
    bst = build_tree(elements)
    print(bst.in_order_traversal())
    print(bst.find_max())
    print(bst.find_min())