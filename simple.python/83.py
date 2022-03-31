# Definition for singly-linked list.
from platform import node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 执行用时：52 ms, 在所有 Python3 提交中击败了14.02%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了36.24%的用户
# 通过测试用例：166 / 166

# 这里传播的都是引用
# 这个方法是遍历法，遍历一遍，空间复杂度O(1),时间复杂度O(n)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head

# 如果遇到了没有sort后的链表该如何处理？

def main():
    cNode = (2)
    bNode = (1,cNode)
    aNode = (1,bNode)
    headNode = ListNode(0, aNode)
    pointNode = headNode
    while pointNode.next :
        print(pointNode.val)
        pointNode = pointNode.next

    a_solution = Solution()
    a_solution.deleteDuplicates(a_listNode)

main()
