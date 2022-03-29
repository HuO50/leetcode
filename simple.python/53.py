from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sublist = nums[0]
        pre = 0
        for num in nums:
            pre = max(pre+num, num)
            max_sublist = max(max_sublist, pre)
        return max_sublist


if __name__ == "__main__":
    asolute = Solution()
    ret = asolute.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(ret)
