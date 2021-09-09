from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        left_part = self.inorderTraversal(root.left)
        right_part = self.inorderTraversal(root.right)
        
        result.extend(left_part)
        result.append(root.val)
        result.extend(right_part)
        return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = []
        pointer = root
        
        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            
            pointer = stack.pop()
            result.append(pointer.val)
            pointer = pointer.right
        
        return result

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