from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(N) space: O(N)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        arr = []
        pointer = head
        while pointer:
            arr.append(pointer.val)
            pointer = pointer.next
        
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
# Follow up: Could you do it in O(n) time and O(1) space?

class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        fast = slow = head
        dummy = None
        while fast and fast.next:
            fast = fast.next.next
            pointer = slow.next
            slow.next = dummy
            dummy = slow
            slow = pointer
        
        if fast:
            slow = slow.next

        while slow:
            if slow.val != dummy.val:
                return False
            slow = slow.next
            dummy = dummy.next
        return True
            
            