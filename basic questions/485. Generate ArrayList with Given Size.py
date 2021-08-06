# Generate an arrayList with given size, initialize the array list with numbers from 1 to size.

class Solution:
    """
    @param size: An integer
    @return: An integer list
    """
    def generate(self, size):
        # write your code here
        return [i + 1 for i in range(size)]