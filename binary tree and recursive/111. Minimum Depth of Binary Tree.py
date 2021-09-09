import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        min_depth = math.inf
        left_part, right_part = math.inf, math.inf
        if root.left:
            left_part = self.minDepth(root.left)
        if root.right:
            right_part = self.minDepth(root.right)
        min_depth = min(left_part, right_part) + 1
        return min_depth

from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0