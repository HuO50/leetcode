from typing import List

# 374ms


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        answer = []
        total = 0
        for i in range(len(A)):
            total = total * 2 + A[i]
            if total % 5 is 0:
                answer.append(True)
            else:
                answer.append(False)
        return answer


# 超时
class Solution2:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        answer = []
        tmp = "0b"
        for i in range(len(A)):
            tmp = tmp + str(A[i])
            calc = str(int(tmp, 2))
            if calc[-1] is '0' or calc[-1] is '5':
                answer.append(True)
            else:
                answer.append(False)
        return answer

# 最好的方法


class Solution3:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        return (n == 0 for n in accumulate(A, lambda x, y: ((x << 1)+y) % 5))


if __name__ == "__main__":
    asolution = Solution2()
    ret = asolution.prefixesDivBy5([0, 1, 1, 1, 1, 1])
    print(ret)
