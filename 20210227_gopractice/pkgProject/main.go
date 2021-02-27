package main

import (
	"fmt"
	"pkgProject/mypkg"
	"pkgProject/mypkg/underpkg"
)

func main() {
	fmt.Println(mypkg.Rectangle(4, 5))
	mypkg.Intro()

	underpkg.Hello()
}
