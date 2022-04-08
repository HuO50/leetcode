from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print()
        if s == None:
            return ""
        a = s[::-1]
        s = a
        print(s)

    # 执行用时：52 ms, 在所有 Python3 提交中击败了22.66%的用户
    # 内存消耗：19.6 MB, 在所有 Python3 提交中击败了36.98%的用户
    # 通过测试用例：477 / 477
    def reverseString2(self, s: List[str]) -> None:
        end = len(s) // 2
        print(end)
        for i in range(0, end):
            tmp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = tmp
        print(s)


def main():
    a_solution = Solution()
    a_solution.reverseString2(["h","e","l","l","o"])
    pass

main()