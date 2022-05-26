# O(n)
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        numbers = self.getArray(root)
        return self.twoSum(numbers, k)
        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return True

            if current_sum > target:
                right -= 1
            else:
                left += 1

        return False
        
        
    def getArray(self, node):
        result = []
        if node.left:
            result.extend(self.getArray(node.left))
        result.append(node.val)
        if node.right:
            result.extend(self.getArray(node.right))
        return result
        