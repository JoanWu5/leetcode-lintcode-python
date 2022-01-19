from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        dummy = pointer = ListNode(-1)
        carry = 0
        
        while l1 or l2:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0
            sum_num = l1_num + l2_num + carry
            
            pointer.next = ListNode(sum_num % 10)
            carry = sum_num // 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            pointer = pointer.next
        
        if carry:
            pointer.next = ListNode(carry)
        
        return self.reverseList(dummy.next)
        
 
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
            
        
# follow up: cannot reverse the list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        
        while curr1:
            curr1 = curr1.next
            n1 += 1
        
        while curr2:
            curr2 = curr2.next
            n2 += 1
        
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1
            
            curr = ListNode(val)
            curr.next = head
            head = curr
        
        curr1, head = head, None
        carry = 0
        while curr1:
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            
            curr = ListNode(val)
            curr.next = head
            head = curr
            
            curr1 = curr1.next
        
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr
        
        return head
                
            
            

        
        
             
        