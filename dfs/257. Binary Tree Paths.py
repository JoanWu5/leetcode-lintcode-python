from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []
        self.dfs(root, [], result)
        return result
    
    def dfs(self, node, expression, result):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            expression.append(str(node.val))
            result.append('->'.join(expression))
            return
        
        self.dfs(node.left, expression + [str(node.val)], result)
        self.dfs(node.right, expression + [str(node.val)], result)

from collections import deque
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []
        queue = deque([(root, [])])
        while queue:
            node, expression = queue.popleft()
            if node.left is None and node.right is None:
                expression.append(str(node.val))
                result.append('->'.join(expression))
                continue
            
            if node.left:
                queue.append((node.left, expression + [str(node.val)]))
            
            if node.right:
                queue.append((node.right, expression + [str(node.val)]))
        return result
