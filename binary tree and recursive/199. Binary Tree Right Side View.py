from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            right_node = None
            for _ in range(level_size):
                node = queue.popleft()
                right_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(right_node.val)
        
        return result

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_part = self.rightSideView(root.right)
        left_part = self.rightSideView(root.left)
        return [root.val] + right_part + left_part[len(right_part):]