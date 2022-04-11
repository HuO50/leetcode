# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 执行用时：68 ms, 在所有 Python3 提交中击败了7.67%的用户
    # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了96.84%的用户
    # 通过测试用例：41 / 41
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next != None:
            node.val =  node.next.val
            node.next = node.next.next
        


def main():
    pass


main()