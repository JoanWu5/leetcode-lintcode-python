from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return None
        
        result = []
        queue = deque([(root, [], targetSum)])
        while queue:
            node, path, num = queue.popleft()
            if node.left is None and node.right is None and num == node.val:
                result.append(path + [node.val])
                continue
            
            if node.left:
                queue.append((node.left, path + [node.val], num - node.val))
            
            if node.right:
                queue.append((node.right, path + [node.val], num - node.val))
        
        return result

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return None
        
        result = []
        def recur(node, path, num):
            if not node:
                return
            
            if node.left is None and node.right is None and node.val == num:
                result.append(path + [node.val])
                return
            
            recur(node.left, path + [node.val], num - node.val)
            recur(node.right, path + [node.val], num - node.val)  
        
        recur(root, [], targetSum)
        return result