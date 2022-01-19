from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(mid)
        return self.mergeList(left, right)
    
    def mergeList(self, left, right):
        if left is None or right is None:
            return left or right
        
        dummy = pointer = ListNode(-1)
        while left and right:
            if left.val <= right.val:
                pointer.next = left
                left = left.next
            else:
                pointer.next = right
                right = right.next
            pointer = pointer.next
            
        pointer.next = left or right
        return dummy.next
        
        