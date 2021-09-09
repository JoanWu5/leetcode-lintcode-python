from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = False
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if self.result or (root.left is None and root.right is None and root.val == targetSum):
            self.result = True
        
        if root.left:
            self.hasPathSum(root.left, targetSum - root.val)
        
        if root.right:
            self.hasPathSum(root.right, targetSum - root.val)
        
        return self.result

from collections import deque


class Solution:
    def __init__(self):
        self.result = False
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, targetSum)])
        while queue:
            node, currentSum = queue.popleft()
            if node.left is None and node.right is None:
                if currentSum == node.val:
                    return True
            
            if node.left:
                queue.append((node.left, currentSum - node.val))
            if node.right:
                queue.append((node.right, currentSum - node.val))
        
        
        return False