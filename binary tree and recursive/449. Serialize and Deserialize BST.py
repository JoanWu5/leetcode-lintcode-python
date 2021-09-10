import math
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        node_list = []
        def preorder(node):
            if not node:
                return
            
            node_list.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return ','.join(node_list)
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        val_list = data.split(',')
        queue = deque(int(val) for val in val_list)
        
        def build(min_val, max_val):
            if queue and min_val < queue[0] < max_val:
                val = queue.popleft()
                node = TreeNode(val)
                node.left = build(min_val, val)
                node.right = build(val, max_val)
                return node
        
        return build(-math.inf, math.inf)
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans