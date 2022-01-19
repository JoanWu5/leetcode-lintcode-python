from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        

        dummy = dummyPointer = ListNode(0)
        previous = head
        
        val = previous.val
        pointer = previous.next
        count = 1
        while pointer:
            if pointer.val == val:
                count += 1
            else:
                if count == 1:
                    dummyPointer.next = previous
                    dummyPointer = dummyPointer.next
                count = 1
                val = pointer.val
                
            previous = pointer
            pointer = pointer.next
        
        if count == 1:
            dummyPointer.next = previous
        else:
            dummyPointer.next = None
            
        return dummy.next