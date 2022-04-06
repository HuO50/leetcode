from typing import List

# 这道题主要使用的位运算的方式进行解答，重新学习了位运算的技巧。
# 交换律：A ^ B = B ^ A;
# 结合律：A ^ (B ^ C) = (A ^ B) ^ C;
# 恒等律：X ^ 0 = X;
# 归零律：X ^ X = 0;
# 自反：A ^ B ^ B = A ^ 0 = A;
# 对于任意的 X： X ^ (-1) = ~X；
# 如果 A ^ B = C 成立，那么 A ^ B = C，B ^ C = A；

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for item in nums:
            res = res ^ item
        return res


def main():
    a = [1,2,3,4,1,2,3]
    a_Solution = Solution()
    print(a_Solution.singleNumber(a))

main()