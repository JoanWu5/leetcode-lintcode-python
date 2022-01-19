from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        pointer = head
        previous = head
        
        while pointer:
            while pointer.next and pointer.val == pointer.next.val:
                pointer = pointer.next
            pointer = pointer.next
            previous.next = pointer
            previous = previous.next
        
        return head
        
# modify:
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        pointer = head.next
        previous = head
        
        while pointer:
            if pointer.val == previous.val:
                previous.next = pointer.next
            else:
                previous = previous.next
                
            pointer = pointer.next
  
        return head