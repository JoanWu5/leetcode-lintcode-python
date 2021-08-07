# Given a binary tree, return the inorder traversal of its nodes‘ values.
# root -> left -> right

# Example:
# Input:
# binary tree = {1,2,3}
# Output:
# [2,1,3]

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
    @return: Inorder in ArrayList which contains node values.
    """
    # recursive
    def inorderTraversal(self, root):
        # write your code here
        self.result = []
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.result.append(root.val)
        self.inorder(root.right)

    # non-recursive
    def inorderTraversal2(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        stack = []
        cur = root
        
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                result.append(node.val)
                cur = node.right
                
        return result
