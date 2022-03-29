from typing import List

#执行用时：28 ms, 在所有 Python3 提交中击败了98.16%的用户
#内存消耗：14.8 MB, 在所有 Python3 提交中击败了16.16%的用户
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        answer = []
        if digits[0] == 0:
            digits[-1] = 1
            return digits

        for i in range(len(digits)):
            total = total * 10 + digits[i]
        total = total + 1

        while (True):
            end = total % 10
            answer.append(end)
            if total < 10:
                break
            total = total // 10
        answer.reverse()
        return answer


if __name__ == "__main__":
    asolute = Solution()
    ret = asolute.plusOne([1, 2, 3])
    print(ret)
