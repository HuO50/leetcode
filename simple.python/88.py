#
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1.copy()

        new_list = []
        count_m = 0
        count_n = 0
        for i in range(0, m + n):
            if count_m >= m:
                new_list = new_list+nums2[count_n:n]
                break
            if count_n > n:
                new_list = new_list + tmp[count_m:m]
                break
            if tmp[count_m] < nums2[count_n]:
                new_list.append(tmp[count_m])
                count_m = count_m + 1
                continue
            if tmp[count_m] == nums2[count_n]:
                new_list.append(tmp[count_m])
                new_list.append(nums2[count_n])
                count_m = count_m + 1
                count_n = count_n + 1
                continue
            if tmp[count_m] > nums2[count_n]:
                new_list.append(nums2[count_n])
                count_n = count_n + 1
                continue
        nums1 = new_list
        print(nums1)


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()
        print(nums1)


if __name__ == "__main__":
    asolution = Solution()
    asolution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
