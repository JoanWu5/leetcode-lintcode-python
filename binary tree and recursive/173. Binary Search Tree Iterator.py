from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.inorderList = []
        self.index = 0
        
        self.inorder = self.inorderTraversel(root)
    
    def inorderTraversel(self, node):
        if not node:
            return []
        
        result = []
        left_part = self.inorderTraversel(node.left)
        right_part = self.inorderTraversel(node.right)
        
        result.extend(left_part)
        result.append(node.val)
        result.extend(right_part)
        return result
        
    def next(self) -> int:
        self.index += 1
        return self.inorder[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.stack = []
        self.pushLeft(root)
    
    def pushLeft(self, node):
        if not node:
            return
        
        while node:
            self.stack.append(node)
            node = node.left
        
    def next(self) -> int:
        node = self.stack.pop()
        self.pushLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0