from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k <= 0:
            return -1
        
        self.k = k
        self.result = None
        self.recur(root)
        return self.result
    
    def recur(self, node):
        if not node:
            return
        self.recur(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self.recur(node.right)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k <= 0:
            return -1
        
        stack = []
        pointer = root

        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            
            pointer = stack.pop()
            k -= 1
            if k == 0:
                return pointer.val
            pointer = pointer.right
        
        return -1