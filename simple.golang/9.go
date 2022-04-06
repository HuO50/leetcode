package main

// 执行用时：12 ms, 在所有 Go 提交中击败了81.54%的用户
// 内存消耗：4.4 MB, 在所有 Go 提交中击败了82.94%的用户

// 计算是否是回文数的方式，就是计算每一位，然后取余最后加出来，
// 加完成之后，看一下 回文计算出来y的与原数x是不是一致
func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	if x > 0 && x%10 == 0 {
		return false
	}

	var y, m int
	for {
		m = x % 10
		y = y*10 + m
		if y >= x || y >= x/10 {
			if y == x || y == x/10 {
				return true
			}
			return false
		}
		x = x / 10
	}

}

func main() {
	println(isPalindrome(1212))
}
