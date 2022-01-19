from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2
        
        pointer1, pointer2 = l1, l2
        dummy = ListNode(0)
        pointer = dummy
        flag = 0
        while pointer1 and pointer2:
            count = pointer1.val + pointer2.val + flag
            node = ListNode(count % 10)
            flag = count // 10
            pointer.next = node
            pointer = pointer.next
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        if pointer1 or pointer2:
            l = pointer1 or pointer2
            while l:
                count = l.val + flag
                node = ListNode(count % 10)
                flag = count // 10
                pointer.next = node
                pointer = pointer.next
                l = l.next
            
        if flag:
            node = ListNode(flag)
            pointer.next = node
        
        return dummy.next

# combine l1 or l2       
# class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2
        
        pointer1, pointer2 = l1, l2
        dummy = ListNode(0)
        pointer = dummy
        flag = 0
        while pointer1 or pointer2:
            x = pointer1.val if pointer1 else 0
            y = pointer2.val if pointer2 else 0
            count = x + y + flag
            flag = count // 10
            
            node = ListNode(count % 10)
            
            pointer.next = node
            pointer = pointer.next
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None
        
            
        if flag:
            node = ListNode(flag)
            pointer.next = node
        
        return dummy.next
                
            