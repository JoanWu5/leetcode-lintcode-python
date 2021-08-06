# Write a function that add two numbers a and b, and return the answer as an integer(int).

class Solution:
    def add(self, a, b):
        return a + b
    
# 主要利用异或运算来完成
# 异或运算有一个别名叫做：不进位加法
# 那么a ^ b就是a和b相加之后，该进位的地方不进位的结果
# 然后下面考虑哪些地方要进位，自然是a和b里都是1的地方
# a & b就是a和b里都是1的那些位置，a & b << 1 就是进位
# 之后的结果。所以：a + b = (a ^ b) + (a & b << 1)
# 令a' = a ^ b, b' = (a & b) << 1
# 可以知道，这个过程是在模拟加法的运算过程，进位不可能 一直持续，所以b最终会变为0。因此重复做上述操作就可以求得a + b的值。
    def aplusb(self, a, b):
        INT_RANGE = pow(2, 32) - 1
        while b != 0:
            a, b = a ^ b, (a & b) << 1
            # python 没有 int 溢出，会自动转成大数进行计算，
            # 可能会因为符号位，导致一直进位超时，所以需要将结果a按二进制位保存下来
            # 由题意可知结果a最多31位，所以INT_RANGE二进制是32个1.
            # 二进制右数第32位记录符号位，右边31位记录数值
            a &= INT_RANGE
        
        return a if a >> 31 <= 0 else a ^ ~INT_RANGE