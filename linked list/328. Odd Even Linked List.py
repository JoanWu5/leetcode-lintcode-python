from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        oddHead, evenHead = ListNode(-1), ListNode(-1)
        oddPointer, evenPointer = oddHead, evenHead
        pointer = head
        count = 1
        
        while pointer:
            if count % 2 == 1:
                oddPointer.next = pointer
                oddPointer = oddPointer.next
            else:
                evenPointer.next = pointer
                evenPointer = evenPointer.next
            pointer = pointer.next
            count += 1
        
        evenPointer.next = None
        oddPointer.next = evenHead.next
        return oddHead.next