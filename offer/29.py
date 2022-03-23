from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        for (; i < len(matrix); i=i+1):
            print(matrix[i][0])


if __name__ == "__main__":
    aSolution = Solution()
    aSolution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
