package main

import (
	"fmt"
)

func swap(x, y string) (string, string) {
	return y, x
}

func main() {
	var a, b string
	a = "hello"
	b = "world"
	c, d := swap(a, b)
	fmt.Println(c, d)
}
