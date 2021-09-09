from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# space: O(N^2)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: root_index], postorder[: root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index: -1])
        return root

# improve space version:  O(N)    
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        
        inorder_dict = {value: index for index, value in enumerate(inorder)}
        self.index = 1
        
        def recur(left, right):
            if left > right:
                return None
            
            root = TreeNode(postorder[-self.index])
            self.index += 1
            
            root_index = inorder_dict[root.val]
            root.right = recur(root_index + 1, right)
            root.left = recur(left, root_index - 1)

            return root
    
        return recur(0, len(inorder) - 1)