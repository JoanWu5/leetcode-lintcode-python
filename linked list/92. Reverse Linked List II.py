from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left >= right:
            return head
        
        pointer = head
        previous = None
        
        for _ in range(left - 1):
            previous = pointer
            pointer = pointer.next
        
        if previous:
            previous.next = None
        
        dummy, tail = self.reverseLinkedList(pointer, right - left + 1)
        
        if previous:
            previous.next = dummy
            
        pointer.next = tail
        return head if previous else dummy
        
        
        
    def reverseLinkedList(self, head, k):
        dummy = None
        pointer = head
        while pointer and k > 0:
            k -= 1
            temp = pointer.next
            pointer.next = dummy
            dummy = pointer
            pointer = temp
        
        return dummy, pointer
        
        