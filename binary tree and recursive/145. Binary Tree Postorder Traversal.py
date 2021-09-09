from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        
        left_part = self.postorderTraversal(root.left)
        right_part = self.postorderTraversal(root.right)
        result.extend(left_part)
        result.extend(right_part)
        result.append(root.val)
        
        return result

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = []
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        
        return result[::-1]