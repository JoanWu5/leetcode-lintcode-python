# Implement a Queue by linked list. Support the following basic methods:

# enqueue(item). Put a new item in the queue.
# dequeue(). Move the first item out of the queue, return it.
# Example:
# Input:
# enqueue(1)
# enqueue(2)
# enqueue(3)
# dequeue() // return 1
# enqueue(4)
# dequeue() // return 2

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        node = LinkedNode(item)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        value = self.head.value
        self.head = self.head.next
        return value

class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    