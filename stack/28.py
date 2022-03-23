

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        try:
            point = haystack.index(needle)
            return point
        except:
            return -1
    
    def strStr2(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        return haystack.find(needle)

    def strStr3(self, haystack: str, needle: str) -> int:
        # 双指针法
        if needle == "":
            return 0
        fast = slow = 0
        while True:
            if haystack[fast] != needle[slow]:
                fast = fast + 1
                slow = 0
            else:
                slow = fast

            




def main():
    str_haystack = "hello"
    str_needle = "llx"
    a_solution = Solution()
    a_solution.strStr3(str_haystack, str_needle)


main()