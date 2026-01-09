# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def sum_tree(root:TreeNode):
            if root.left:
                sum_tree(root.left)
                root.val+= root.left.val
            if root.right:
                sum_tree(root.right)
                root.val+= root.right.val
        sum_tree(root)

        whole = root.val; half = whole // 2
        while True:
            a = root.left.val if root.left else 0
            if a > half:
                root = root.left
                continue
            b = root.right.val if root.right else 0
            if b > half:
                root = root.right
                continue
            return max((whole-x)*x for x in [a,b,root.val]) % 1_000_000_007
    

engine = Solution()



