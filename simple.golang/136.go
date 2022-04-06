package main

// 执行用时：12 ms, 在所有 Go 提交中击败了93.57%的用户
// 内存消耗：6 MB, 在所有 Go 提交中击败了74.75%的用户
// 通过测试用例：61 / 61

func singleNumber(nums []int) int {
	var res, i int
	res = 0
	for i = 0; i < len(nums); i++ {
		res = res ^ nums[i]
	}
	return res
}

func main() {
	//var a []int
	a := [7]int{1, 2, 3, 4, 1, 2, 3}
	singleNumber(a)
}
