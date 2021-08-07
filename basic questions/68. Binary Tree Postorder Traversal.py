# Given a binary tree, return the postorder traversal of its nodes’ values.
# left -> right -> root

# Example:
# Input:
# binary tree = {1,2,3}
# Output:
# [2,3,1]

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    # recursive
    def postorderTraversal(self, root):
        # write your code here
        self.result = []
        self.postorder(root)
        return self.result
    
    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.result.append(root.val)

        # non-recursive
    def postorderTraversal2(self, root):
        # write your code here
        result = []
        if root is None:
            return result
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