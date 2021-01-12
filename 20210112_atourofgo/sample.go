package main

import (
	"fmt"
	"math"
	"math/rand"
)

func main() {
	fmt.Println("a Tour of Go 開始")
	packages()
	imports()
	exportnames()
	functons1()
	functons2()
	fmt.Println("a Tour of Go 終了")
}

func packages() {
	fmt.Println(" ")
	fmt.Println("1.Packages")
	fmt.Println("My favorite number is", rand.Intn(10))
}

func imports() {
	fmt.Println(" ")
	fmt.Println("2.Imports")
	fmt.Printf("Now you have %g problems.\n", math.Sqrt(7))
}

func exportnames() {
	fmt.Println(" ")
	fmt.Println("3.ExportNames")
	fmt.Println(math.Pi)

}

func functons1() {
	fmt.Println(" ")
	fmt.Println("4.Function1")
	fmt.Println(add1(42, 13))
}

func add1(x int, y int) int {
	return x + y
}

func functons2() {
	fmt.Println(" ")
	fmt.Println("5.Function2")
	fmt.Println(add2(42, 13))
}
func add2(x, y int) int {
	return x + y
}