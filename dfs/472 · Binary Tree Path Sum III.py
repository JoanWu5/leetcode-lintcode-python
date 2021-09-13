"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        self.result = []
        self.dfs(root, target)
        return self.result
    
    def dfs(self, node, target):
        if node is None:
            return
        
        self.dfs2(node, None, target, [])
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    def dfs2(self, node, pre_node, target, path):
        if node is None:
            return
        
        path.append(node.val)
        target -= node.val
        if target == 0:
            self.result.append(list(path))
        
        if node.parent not in [pre_node, None]:
            self.dfs2(node.parent, node, target, path)
        
        if node.left not in [pre_node, None]:
            self.dfs2(node.left, node, target, path)

        if node.right not in [pre_node, None]:
            self.dfs2(node.right, node, target, path)
        
        path.pop()
        target += node.val

        

        
