package main

import "fmt"

func mySqrt(x int) int {
	var a int
	a = 0
	for {
		if (a+1)*(a+1) > x {
			return a
		}
		a++
	}
}

func mySqrt_newton(x int) int {
	var ans int
	ans = x
	for {
		if ans*ans <= x {
			break
		}
		ans = (ans + x/ans) / 2
	}
	return ans + 1
}

func main() {
	var result int
	result = mySqrt_newton(9)
	fmt.Println(result)
}
