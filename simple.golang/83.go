/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// 执行用时：4 ms, 在所有 Go 提交中击败了76.88%的用户
// 内存消耗：3 MB, 在所有 Go 提交中击败了72.32%的用户
// 通过测试用例：166 / 166
func deleteDuplicates(head *ListNode) *ListNode {
	var node *ListNode
	node = head
	if node == nil {
		return nil
	}

	for true {
		if node.Next == nil {
			break
		}
		if node.Val == node.Next.Val {
			node.Next = node.Next.Next
		} else {
			node = node.Next
		}
	}
	return head
}

func main() {

}