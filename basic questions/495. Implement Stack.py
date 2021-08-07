# Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

# Example:
# Input:
# push(1)
# pop()
# push(2)
# top()  // return 2
# pop()
# isEmpty() // return true
# push(3)
# isEmpty() // return false

class Stack:
    def __init__(self):
        self.stack = []

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.stack.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.stack.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return  len(self.stack) == 0
