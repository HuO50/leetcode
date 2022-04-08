class Solution:
    # 执行用时：36 ms, 在所有 Python3 提交中击败了61.14%的用户
    # 内存消耗：14.8 MB, 在所有 Python3 提交中击败了81.19%的用户
    # 通过测试用例：60 / 60
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True


def main():
    pass

main()