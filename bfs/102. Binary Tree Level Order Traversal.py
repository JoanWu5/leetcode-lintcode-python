# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

# bfs
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque()
        queue.append(root)
        
        while queue:
            levelSize = len(queue)
            level = []
            for _ in range(levelSize):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

# dfs
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root, l = 0):
            if not root:
                return
            if len(result) <= l:
                result.append([root.val])
            else:
                result[l].append(root.val)
            dfs(root.left, l + 1)
            dfs(root.right, l + 1)
        
        result = []
        dfs(root)
        return result