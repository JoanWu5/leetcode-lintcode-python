from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = []
        pointer = root
        previousNum = None
        
        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            
            pointer = stack.pop()
            
            if previousNum is None or previousNum < pointer.val:
                previousNum = pointer.val
            else:
                return False
            
            pointer = pointer.right
        
        return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, -math.inf, math.inf)
    
    def checkBST(self, root: Optional[TreeNode], left, right) -> bool:
        if not root:
            return True
        if not left < root.val < right:
            return False
        return self.checkBST(root.left, left, root.val) and self.checkBST(root.right, root.val, right)
                
            
                
            