class Solution:
    #执行用时：3464 ms, 在所有 Python3 提交中击败了5.04%的用户
    #内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.39%的用户
    def mySqrt(self, x: int) -> int:
        i = 0
        while(i*i<=x):
            if (i+1) * (i+1) > x:
                return i
            i = i+1
 

def main():
    a_solution = Solution()
    print(a_solution.mySqrt(4))
    pass

main()