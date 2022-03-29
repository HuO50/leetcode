# 119 杨辉三角
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        print(rowIndex)
        gen = self.getNewRow()
        res = []
        for i in range(rowIndex):
            res.append(gen.__next__().copy())
        return res

    def getNewRow(self):
        ret = [1]
        while True:
            yield ret
            for i in range(1, len(ret)):
                ret[i] = pre[i] + pre[i - 1]
            ret.append(1)
            pre = ret[:]


if __name__ == "__main__":
    solute = Solution()
    result = solute.getRow(4)
    print(result)
