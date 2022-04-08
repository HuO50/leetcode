package main

// 执行用时：20 ms, 在所有 Go 提交中击败了99.92%的用户
// 内存消耗：6.4 MB, 在所有 Go 提交中击败了71.41%的用户
// 通过测试用例：477 / 477
func reverseString(s []byte) {
	var end int
	end = len(s) / 2
	var i int
	var tmp byte
	for i = 0; i < end; i++ {
		tmp = s[i]
		s[i] = s[len(s)-i-1]
		s[len(s)-i-1] = tmp
	}
}
