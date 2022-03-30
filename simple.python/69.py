class Solution:
    #执行用时：3464 ms, 在所有 Python3 提交中击败了5.04%的用户
    #内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.39%的用户
    def mySqrt(self, x: int) -> int:
        i = 0
        while(i*i<=x):
            if (i+1) * (i+1) > x:
                return i
            i = i+1

    # 二分法
    def mySqrt2(self, x: int) -> int:
        l = 0
        r = x
        while ((r-l) >1):
            mid = (l + r)//2
            if (mid * mid) >= x:
                r = mid - 1
            else:
                l = mid + 1
        return l

    # 牛顿法
    # 执行用时：48 ms, 在所有 Python3 提交中击败了34.09%的用户
    # 内存消耗：14.8 MB, 在所有 Python3 提交中击败了86.41%的用户
    def mySqrt_newton(self, x: int) -> int:
        ans = x
        while (ans * ans > x):
            ans = (ans + x/ans) // 2 # 如果是 /2 的话，这里需要判断精度，如果是// 2的话，则是整数
        return int(ans)

def main():
    a_solution = Solution()
    print(a_solution.mySqrt_newton(5))
    pass

main()