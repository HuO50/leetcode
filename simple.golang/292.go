
// 执行用时：0 ms, 在所有 Go 提交中击败了100.00%的用户
// 内存消耗：1.8 MB, 在所有 Go 提交中击败了44.84%的用户
// 通过测试用例：60 / 60
func canWinNim(n int) bool {
	if n%4 == 0 {
		return false
	} else {
		return true
	}
}