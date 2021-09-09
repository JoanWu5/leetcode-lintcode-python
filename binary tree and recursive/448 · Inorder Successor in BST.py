"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        
        stack = []
        pointer = root
        find = False

        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            
            pointer = stack.pop()
            if find:
                return pointer

            if pointer == p:
                find = True

            pointer = pointer.right
        
        return None

# recursive
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        
        left = self.inorderSuccessor(root.left, p)
        return left if left else root

# not recursive not using stack  
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        
        successor = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor