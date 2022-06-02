# O(mn)
class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if nums1 == "0" or nums2 == "0":
            return "0"

        n = len(nums1) + len(nums2)
        result = [0] * n

        for pointer1 in range(len(nums1) - 1, -1, -1):
            for pointer2 in range(len(nums2) - 1, -1, -1):
                nums_zeros = pointer1 + pointer2 + 1
                multiplier = (ord(nums1[pointer1]) - ord('0')) * \
                    (ord(nums2[pointer2]) - ord('0')) + result[nums_zeros]

                result[nums_zeros] = multiplier % 10
                result[nums_zeros - 1] += multiplier // 10

        for i in range(len(result)):
            if result[i] != 0:
                result = result[i:]
                break

        return "".join(str(digit) for digit in result)
