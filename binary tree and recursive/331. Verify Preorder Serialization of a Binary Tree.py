class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot
        if not preorder:
            return True
        
        node_list = preorder.split(',')
        slot = 1
        for node in node_list:
            if slot == 0:
                return False
            
            if node == "#":
                slot -= 1
            else:
                slot += 1
        
        return slot == 0


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        
        node_list = preorder.split(',')
        stack = []
        for elem in node_list:
            stack.append(elem)
            while len(stack) > 2 and stack[-2:] == ["#"]*2 and stack[-3] != "#":
                stack.pop(-3)
                stack.pop(-2)
            
        return stack == ["#"]