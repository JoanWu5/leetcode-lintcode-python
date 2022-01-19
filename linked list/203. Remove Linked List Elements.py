from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = pointer = ListNode(-1)
        while head:
            if head.val != val:
                pointer.next = head
                pointer = pointer.next
            head = head.next
        
        pointer.next = None
        return dummy.next
                