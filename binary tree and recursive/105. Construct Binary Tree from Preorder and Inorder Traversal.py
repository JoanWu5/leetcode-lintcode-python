from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break
        root.left = self.buildTree(preorder[1: i + 1], inorder[: i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        
        inorder_dict = {value: index for index, value in enumerate(inorder)}
        self.index = 0
        
        def recur(left, right):
            if left > right:
                return None
            
            root = TreeNode(preorder[self.index])
            self.index += 1
            
            root_index = inorder_dict[root.val]
            root.left = recur(left, root_index - 1)
            root.right = recur(root_index + 1, right)
            return root
        
        return recur(0, len(inorder) - 1)