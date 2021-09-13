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
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        
        result = []
        self.dfs(root, [], target, result)
        return result
        
    def dfs(self, node, path, target, result):
        if node.left is None and node.right is None and target == node.val:
            path.append(node.val)
            result.append(path)
            return
        
        if node.left:
            self.dfs(node.left, path + [node.val], target - node.val, result)
        
        if node.right:
            self.dfs(node.right, path + [node.val], target - node.val, result)
