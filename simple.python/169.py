from typing import List

class Solution:
    #执行用时：44 ms, 在所有 Python3 提交中击败了65.17%的用户
    #内存消耗：16.5 MB, 在所有 Python3 提交中击败了13.18%的用户
    #通过测试用例：43 / 43
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]

    # hash 法，但是中间list 长度不知道怎么声明
    # 执行用时：84 ms, 在所有 Python3 提交中击败了5.23%的用户
    # 内存消耗：16.4 MB, 在所有 Python3 提交中击败了34.03%的用户
    # 通过测试用例：43 / 43
    def majorityElement2(self, nums: List[int]) -> int:
        hash_list = [None] * 100000
        res = None
        for i in range(0, len(nums)):
            if not hash_list[nums[i]]:
                hash_list[nums[i]] = 1
            else:
                hash_list[nums[i]] = hash_list[nums[i]] + 1
            print(hash_list[nums[i]])
            if hash_list[nums[i]] > len(nums)/2:
                res = nums[i]
                break
        return res

    # 摩尔投票


def main():
    a_solution = Solution()
    print(a_solution.majorityElement2([3,2,3]))


main()