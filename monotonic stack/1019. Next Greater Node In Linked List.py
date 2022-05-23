from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# stack: O(N) space: O(N)
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []

        stack = []
        result = []

        pointer = head
        while pointer:
            result.append(0)
            pointer = pointer.next

        pointer = head
        counter = 0
        while pointer:
            while stack and pointer.val > stack[-1][0]:
                _, index = stack.pop()
                result[index] = pointer.val

            stack.append((pointer.val, counter))
            pointer = pointer.next
            counter += 1

        return result
