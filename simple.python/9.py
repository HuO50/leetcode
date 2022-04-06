from audioop import reverse


class Solution:
    # python3 字符串反转的两种方法，第一种更好用，字符串切片
    def isPalindrome(self, x: int) -> bool:
        print(str(x)[::-1])
        print(''.join(reversed( str(x))))
        return x>-1 and str(x)[::-1]==str(x)

    # 转化成为数组，然后使用双指针进行前后扫，同时进行扫描的话，会比较方便

def main():
    a_solution = Solution()
    print(a_solution.isPalindrome(121))

main()