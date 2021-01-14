#
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_tmp = nums1.copy()
        nums1 = []
        count_m = 0
        count_n = 0
        for i in range(0, m + n):
            if count_m >= m:
                nums1 = nums1+nums2[count_n:n]
                break
            if count_n > n:
                nums1 = nums1 + nums1_tmp[count_m:m]
                break
            if nums1_tmp[count_m] < nums2[count_n]:
                nums1.append(nums1_tmp[count_m])
                count_m = count_m + 1
                continue
            if nums1_tmp[count_m] == nums2[count_n]:
                nums1.append(nums1_tmp[count_m])
                nums1.append(nums2[count_n])
                count_m = count_m + 1
                count_n = count_n + 1
                continue
            if nums1_tmp[count_m] > nums2[count_n]:
                nums1.append(nums2[count_n])
                count_n = count_n + 1
                continue
        print(nums1)


if __name__ == "__main__":
    asolution = Solution()
    ret = asolution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
