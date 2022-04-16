class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #执行用时：36 ms, 在所有 Python3 提交中击败了84.12%的用户
    #内存消耗：16 MB, 在所有 Python3 提交中击败了77.08%的用户
    #通过测试用例：28 / 28
    def reverseList(self, head: ListNode) -> ListNode:
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev

def main():
    pass

main()