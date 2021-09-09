from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isSymmetricTree(root.left, root.right)
    
    def isSymmetricTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.isSymmetricTree(root1.left, root2.right) and self.isSymmetricTree(root1.right, root2.left)

from collections import deque

class Solution:
    def checkTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return True
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        while queue:
            left, right = queue.popleft()
            if not self.checkTree(left, right):
                return False
            
            if left:
                queue.append((left.left, right.right))
                queue.append((left.right, right.left))
        
        return True
            
        