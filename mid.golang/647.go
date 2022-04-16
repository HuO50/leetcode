package main

// 执行用时：0 ms, 在所有 Go 提交中击败了100.00%的用户
// 内存消耗：1.8 MB, 在所有 Go 提交中击败了84.58%的用户
// 通过测试用例：130 / 130
func countSubstrings(s string) int {
	ans := 0
	n := len(s)

	for i := 0; i < 2*n-1; i++ { // 1.第一个地方就是 2n-1 这里需要进行思考原因：
		l, r := i/2, i/2+i%2                  // 2.这里的左右边界需要进行讨论
		for l >= 0 && r < n && s[l] == s[r] { // 3.这里判断的内容是 如何算是一个成功的子串
			l--
			r++
			ans++
		}
	}
	return ans
}

// 执行用时：0 ms, 在所有 Go 提交中击败了100.00%的用户
// 内存消耗：1.9 MB, 在所有 Go 提交中击败了70.21%的用户
// 通过测试用例：130 / 130
func countSubstrings2(s string) int {
	ans := 0
	n := len(s)

	for i := 0; i < n; i++ {
		l := i
		r := i
		for l >= 0 && r < n && s[l] == s[r] {
			l--
			r++
			ans++
		}
		//
		l = i
		r = i + 1
		for l >= 0 && r < n && s[l] == s[r] {
			l--
			r++
			ans++
		}
	}
	return ans
}

func main() {
	println(countSubstrings2("abc"))
}
