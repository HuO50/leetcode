# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归遍历方法
# 执行用时：36 ms, 在所有 Python3 提交中击败了62.32%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了39.76%的用户
# 通过测试用例：70 / 70
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        
        pass

def main():
    pass

main()