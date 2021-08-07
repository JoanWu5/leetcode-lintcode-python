class Solution:
    """
    @param target: A string
    @return: An integer
    """
    def stringToInteger(self, target):
        # write your code here
        is_negative = False
        result = 0
        if target[0] == "-":
            is_negative = True
        for char in target:
            if char != "-":
                result = 10 * result + ord(char) - ord('0')
        return -result if is_negative else result