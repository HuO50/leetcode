from typing import List

class Solution:
    #执行用时：64 ms, 在所有 Python3 提交中击败了48.21%的用户
    #内存消耗：25.5 MB, 在所有 Python3 提交中击败了47.63%的用户
    #通过测试用例：70 / 70
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) < len(len(nums)):
        #     return False
        # else:
        #     return True

        return True if len(set(nums)) < len(nums) else False

def main():
    a_solution = Solution()
    a_solution.containsDuplicate([1,2,3,1])

main()