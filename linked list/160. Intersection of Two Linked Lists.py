# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        pointer1, pointer2 = headA, headB
        while pointer1 != pointer2:
            pointer1 = pointer1.next if pointer1 else headB
            pointer2 = pointer2.next if pointer2 else headA
        
        return pointer1
                