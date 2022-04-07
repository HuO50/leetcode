#import math

class Solution:
    #执行用时：40 ms, 在所有 Python3 提交中击败了48.05%的用户
    #内存消耗：14.8 MB, 在所有 Python3 提交中击败了82.07%的用户
    #通过测试用例：1108 / 1108
    # 这里的方式是通过n & n-1 == 0 这个位运算的方式进行的，所以这个方法特别直接
    # 例如： 8 的二进制代码是1000 ， 7的二进制代码是0111，两个方法求& == 0
    # 因为n-1 是把其他位数都变成1，这样就可以通过&计算的方式，进行计算。
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and ((n & n-1) ==0)

    # 执行用时：32 ms, 在所有 Python3 提交中击败了89.14%的用户
    # 内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.85%的用户
    # 通过测试用例：1108 / 1108
    def isPowerOfTwo2(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n%2!=0:
            return False
        else:
            return self.isPowerOfTwo2(n/2)

    # 执行用时：44 ms, 在所有 Python3 提交中击败了22.83%的用户
    # 内存消耗：14.9 MB, 在所有 Python3 提交中击败了41.62%的用户
    # 通过测试用例：1108 / 1108
    # 利用补码计算 比如8的原码是01000，8的反码是-8，也就是11000，8的补码是11001
    # 
    def isPowerOfTwo3(self, n: int) -> bool:
        return n > 0 and ((n & -n) ==n)

def main():
    a_solution = Solution()
    print(a_solution.isPowerOfTwo3(5))

main()