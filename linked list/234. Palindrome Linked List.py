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
        if not head or not head.next:
            return True
        
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        first_half_end = slow
        second_half_start = self.reverseList(first_half_end.next)
        
        first_half = head
        second_half = second_half_start
        result = True
        
        while result and second_half:
            if first_half.val != second_half.val:
                result = False
            first_half = first_half.next
            second_half = second_half.next
        
        first_half_end = self.reverseList(second_half_start)
        return result
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = None
        while head:
            next_node = head.next
            head.next = dummy
            dummy = head
            head = next_node
        return dummy
            
            
            