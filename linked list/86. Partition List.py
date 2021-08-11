from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        greaterHead = greaterPointer = ListNode(-1)
        lessHead = lessPointer = ListNode(-1)
        
        pointer = head
        while pointer:
            if pointer.val < x:
                lessPointer.next = pointer
                lessPointer = lessPointer.next
            else:
                greaterPointer.next = pointer
                greaterPointer = greaterPointer.next
            pointer = pointer.next
        
        greaterPointer.next = None
        lessPointer.next = greaterHead.next
        return lessHead.next
                
        