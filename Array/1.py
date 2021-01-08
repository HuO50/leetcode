class Solution:

    def two_sum(self, nums, target):
        """这样写更直观，遍历列表同时查字典"""
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i
