from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while (True):
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] == target:
                return mid
            # 判断左右是否到达相同位置
            if left == right:
                return left
            if target > nums[left] and target < nums[mid]:
                right = mid
                mid = (left + right) // 2
                left = left + 1
                continue
            if target > nums[mid] and target < nums[right]:
                left = mid
                mid = (left + right) // 2
                right = right + 1
                continue


if __name__ == "__main__":
    asolute = Solution()
    ret = asolute.searchInsert([1, 3, 5, 6], 5)
    print(ret)
