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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        flag = True
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            
            if flag:
                result.append(level)
            else:
                result.append(level[::-1])
            flag = not flag
        return result

# dfs
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, l = 0):
            if not root:
                return
            if len(result) <= l:
                result.append([root.val])
            else:
                if l % 2 == 0:
                    result[l].append(root.val)
                else:
                    result[l].insert(0, root.val)
            dfs(root.left, l + 1)
            dfs(root.right, l + 1)
        
        result = []
        dfs(root)
        return result