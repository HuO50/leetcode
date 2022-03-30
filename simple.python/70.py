class Solution:

    # 递归法
    # 第n层，可以由第n-1层踏1步上楼， 可以由第n-2层踏2步上楼
    # 以第3层为例：第3层可以从第1层踏2步到达，也可以从第2层踏1步到达；
    # 1.因为到达了第1层的时候，踏2步这个动作是固定的，所以从第1层，通过踏2步上第3层这个算法就是固定
    # 所以这里，只要算出到达1层所需要用的方法，就可以知道它踏步方法
    # 2.同样的道理，可以计算第2层踏1步的方法来达到第3层。
    # 所以得到一个结论，到达第3层的方法是由到达第2层和到达第1层的方法同时确定出来的。也就是d[n] = d[n-1]+dn[n-2]
    # 如此进行统计的，一直到最下边的第1层和第2层。中间迭代加了无数个第1层和无数个第2层
    # 这个方法的空间复杂度比较高
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        print(n)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 执行用时：36 ms, 在所有 Python3 提交中击败了57.93%的用户
    # 内存消耗：15 MB, 在所有 Python3 提交中击败了30.46%的用户
    def climbStairs2(self, n: int) -> int:
        list_n = []
        list_n.append(0)
        list_n.append(1)
        list_n.append(2)
        for item in range(3, n+1):
            list_n.append(list_n[item - 1] + list_n[item - 2])
        return list_n[n]


def main():
    a_solution = Solution()
    print(a_solution.climbStairs2(44))

    pass


main()