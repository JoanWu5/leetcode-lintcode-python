import math
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
        self.result = -math.inf
    
        def recur(node):
            if not node:
                return 0
            left_part = max(recur(node.left), 0)
            right_part = max(recur(node.right), 0)
            current_max = left_part + node.val + right_part
            self.result = max(self.result, current_max)
            
            return node.val + max(left_part, right_part)
        
        recur(root)
        return self.result