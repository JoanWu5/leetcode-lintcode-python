from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

       
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, 2 * interval):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]
                                        
    
    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2
        
        dummy = pointer = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            
            pointer = pointer.next
            
        if l1 or l2:
            pointer.next = l1 or l2
        
        return dummy.next