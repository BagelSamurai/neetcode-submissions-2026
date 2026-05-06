# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. If BOTH are empty, they are the same.
        if not p and not q:
            return True
            
        # 2. If ONLY ONE is empty (or they both exist but values differ), they are not the same.
        if not p or not q or p.val != q.val:
            return False
            
        # 3. If the current nodes match, recursively check the left AND right children.
        # Notice the use of 'self.' here!
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)