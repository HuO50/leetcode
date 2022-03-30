package main

import "fmt"

// 执行用时：0 ms, 在所有 Go 提交中击败了100.00%的用户
// 内存消耗：1.8 MB, 在所有 Go 提交中击败了85.77%的用户
func climbStairs(n int) int {
	var list_n [100]int
	list_n[0] = 0
	list_n[1] = 1
	list_n[2] = 2
	var i int
	for i = 3; i < n+1; i++ {
		list_n[i] = list_n[i-1] + list_n[i-2]
	}
	return list_n[n]
}

func main() {
	fmt.Println(climbStairs(30))
}
