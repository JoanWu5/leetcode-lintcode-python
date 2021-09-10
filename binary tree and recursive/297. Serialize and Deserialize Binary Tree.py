# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "null"
        
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append("null")
        
        return ','.join(result)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "null":
            return None
        
        data = data.split(',')
        root = TreeNode(data[0])
        n = len(data)
        
        queue = deque()
        queue.append(root)
        count = 0
        
        while queue:
            node = queue.popleft()
            if count * 2 + 1 < n and data[2 * count + 1] != "null":
                node.left = TreeNode(int(data[2 * count + 1]))
                queue.append(node.left)
            if count * 2 + 2 < n and data[2 * count + 2] != "null":
                node.right = TreeNode(int(data[2 * count + 2]))
                queue.append(node.right)
            count += 1
        
        return root
            
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if root is None:
                result.append("null")
                return
            
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
    
        result = []
        dfs(root)
        return ','.join(result)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "null":
            return None
        
        data = data.split(',')
        n = len(data)
        self.i = 0
        
        def dfs():
            if self.i == n:
                return None
            if data[self.i] == "null":
                self.i += 1
                return None
            
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
            
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))