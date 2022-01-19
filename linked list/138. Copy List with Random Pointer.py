# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        NodeDict = dict()
        dummy = dummyPointer = Node(-1)
        
        pointer = head
        while pointer:
            dummyPointer.next = Node(pointer.val)
            dummyPointer = dummyPointer.next
            NodeDict[pointer] = dummyPointer
            pointer = pointer.next
        
        pointer = head
        while pointer:
            if pointer.random:
                NodeDict[pointer].random = NodeDict[pointer.random]
            pointer = pointer.next
                 
        return dummy.next
        
            
        
        