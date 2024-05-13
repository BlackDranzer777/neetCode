# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        target = 0
        node = root
        def dfs(node, target):
            if not node:
                return False
            
            target+=node.val
            
            if not node.left and not node.right and target == targetSum:
                return True
            
            if dfs(node.left, target):
                return True

            if dfs(node.right, target):
                return True

            return False

        return dfs(root, target)
        