class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if ' ' not in s:
            return len(s)

        letter_split = s.split(' ')
        replace_split = [ i for i in letter_split if i != "" ]
        return len(replace_split[-1])
        
    def lengthOfLastWord2(self, s: str) -> int:
        if ' ' not in s:
            return len(s)

        letter_split = s.split(' ')
        letter_split.reverse()
        for item in letter_split:
            if item != "":
                return len(item)


def main():
    a_solution = Solution()
    print(a_solution.lengthOfLastWord2("  hello world  "))



main()
