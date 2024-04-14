# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        
        
        #using iterative method
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            nodes.append(cur.val)
            cur=cur.right
        return nodes


        #using recursive method
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            nodes.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return nodes
        