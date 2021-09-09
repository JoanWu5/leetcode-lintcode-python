from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = True
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.heightofTree(root) != -1
    
    def heightofTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.heightofTree(root.left)
        if left_height == -1:
            return -1
        right_height = self.heightofTree(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

class Solution:
    def __init__(self):
        self.result = True
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, False)]
        depths = {None: 1}
        
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            
            if not visited:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                left, right = depths[node.left], depths[node.right]
                if left == -1 or right == -1 or abs(left - right) > 1:
                    depths[node] = -1
                else:
                    depths[node] = max(left, right) + 1
        
        return depths[root] != -1
                
            
        