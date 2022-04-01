/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []
	}else{
		return inorderTraversal(root.Left) + [root.Val] + inorderTraversal(root.Right)
	}
}