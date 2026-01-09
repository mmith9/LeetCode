# Definition for a binary tree node.
from typing import Optional, Tuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dig_tree(node:TreeNode) -> Tuple[TreeNode, int]:
            if not node:
                return None, 0

            anode, a = dig_tree(node.left)
            bnode, b = dig_tree(node.right)

            if a > b:
                return anode, a + 1
            if b > a:
                return bnode, b + 1
            return node, a + 1
        
        return dig_tree(root)[0]

            
        