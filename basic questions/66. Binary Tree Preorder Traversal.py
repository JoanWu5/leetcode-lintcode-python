# Given a binary tree, return the preorder traversal of its nodes' values.
# left -> root -> right
# Example:
# input :{1,2,3,4,5}
# output: [1,2,4,5,3]


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# recursive
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        self.result = []
        self.preorder(root)
        return self.result
    
    def preorder(self, root):
        if root is None:
            return
        self.result.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

# non-recursive
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
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