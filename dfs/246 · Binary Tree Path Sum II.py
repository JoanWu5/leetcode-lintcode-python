"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        self.result = []
        self.dfs(root, target)
        return self.result
    
    def dfs(self, node, target):
        if node is None:
            return
        
        self.dfs2(node, target, [], 0)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    def dfs2(self, node, target, path, current):
        if node is None:
            return
        
        path.append(node.val)
        current += node.val
        if current == target:
            self.result.append(list(path))
        
        self.dfs2(node.left, target, path, current)
        self.dfs2(node.right, target, path, current)
        path.pop()
        current -= node.val
        