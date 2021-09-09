from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder or len(preorder) != len(postorder):
            return None
        
        root = TreeNode(preorder[0])
        if len(postorder) == 1:
            return root
        right_index = preorder.index(postorder[-2])
        
        root.left = self.constructFromPrePost(preorder[1: right_index], postorder[: right_index - 1])
        root.right = self.constructFromPrePost(preorder[right_index:], postorder[right_index - 1: -1])
        return root

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder or len(preorder) != len(postorder):
            return None
        
        self.index = 1
        preorder_dict = {value: index for index, value in enumerate(preorder)}
        def recur(left, right):
            if left > right:
                return None
            
            root = TreeNode(postorder[-self.index])
            self.index += 1
            
            if left == right:
                return root
            
            right_index = preorder_dict[postorder[-self.index]]
            
            root.right = recur(right_index, right)
            root.left = recur(left + 1, right_index - 1)
            return root
        
        return recur(0, len(preorder) - 1)