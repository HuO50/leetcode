
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)+1

        nums.append(target)
        nums.sort()
        return nums.index(target)+1



def main():
    nums=[1,2,3,4,5,6,7]
    target=8
    a_solution = Solution()
    result = a_solution.searchInsert(nums, target)
    print(result)

main()