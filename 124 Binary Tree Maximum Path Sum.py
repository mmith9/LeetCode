# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_path = root.val

        def traverse(root:TreeNode):
            nonlocal max_path            
            center = root.val
            left = traverse(root.left) if root.left else 0
            right = traverse(root.right) if root.right else 0
            
            ret = max(center, left+center, right+center)
            max_path = max(max_path, left+center+right, ret)
            return ret
    
        traverse(root)

        return max_path