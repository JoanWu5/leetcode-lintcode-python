from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        result.append(root.val)
        
        left_part = self.preorderTraversal(root.left)
        right_part = self.preorderTraversal(root.right)
        result.extend(left_part)
        result.extend(right_part)
        
        return result

        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = []
        
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
                