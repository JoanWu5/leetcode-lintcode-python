class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        pointer1, pointer2 = n1 - 1, n2 - 1
        result = 0
        flag = 0
        count1 = 1
        
        while pointer1 >= 0:
            pointer2 = n2 - 1
            count2 = 1
            while pointer2 >= 0:
                multiplier = (ord(num1[pointer1]) - ord('0')) * (ord(num2[pointer2]) - ord('0')) + flag
                
                flag = multiplier // 10
                result += (multiplier % 10) * count1 * count2
                count2 *= 10
                pointer2 -= 1
                
            result += flag * count1 * count2
            pointer1 -= 1
            count1 *= 10
            flag = 0
        
        
        return str(result)