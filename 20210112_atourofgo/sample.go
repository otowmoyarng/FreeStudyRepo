package main

import (
	"fmt"
	"math"
	"math/rand"
	"math/cmplx"
)

func main() {
	fmt.Println("a Tour of Go 開始")
	packages()
	imports()
	exportnames()
	functons1()
	functons2()
	multipleresults()
	nameReturnVaue()
	variables()
	variableInitialize()
	shortVariableDecoration()
	basicType()
	zeroValues()
	typeConversions()
	typeInference()
	constants()
	numericConstants()

	fmt.Println(" ")
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

func multipleresults() {
	fmt.Println(" ")
	fmt.Println("6.MultipleResults")
	a, b := swap("hello", "world")
	fmt.Println(a, b)
}

func swap(x, y string) (string, string) {
	return y, x
}

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func nameReturnVaue() {
	fmt.Println(" ")
	fmt.Println("7.NameReturnVaue")
	fmt.Println(split(17))
}

var c, python, java bool

func variables() {
	fmt.Println(" ")
	fmt.Println("8.Variables")
	var i int
	fmt.Println(i, c, python, java)
}

var i, j int = 1, 2
func variableInitialize() {
	fmt.Println(" ")
	fmt.Println("9.VariableInitialize")
	var c1, python1, java1 = true, false, "no!"
	fmt.Println(i, j, c1, python1, java1)
}

func shortVariableDecoration() {
	fmt.Println(" ")
	fmt.Println("10.ShortVariableDecoration")
	//var i, j int = 1, 2
	k := 3
	c2, python2, java2 := true, false, "no!"

	fmt.Println(i, j, k, c2, python2, java2)
}

var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)
func basicType() {
	fmt.Println(" ")
	fmt.Println("11.BasicType")
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}

func zeroValues() {
	fmt.Println(" ")
	fmt.Println("12.ZeroValues")
	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s)
}

func typeConversions() {
	fmt.Println(" ")
	fmt.Println("13.TypeConversions")
	var x, y int = 3, 4
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f)
	fmt.Println(x, y, z)
}

func typeInference() {
	fmt.Println(" ")
	fmt.Println("14.TypeInference")
	i := 42
	fmt.Printf("i is of type %T\n", i)
	f := 3.14
	fmt.Printf("f is of type %T\n", f)
}

const Pi = 3.14
func constants() {
	fmt.Println(" ")
	fmt.Println("15.Constants")
	const World = "世界"
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)
}

const (
	// Create a huge number by shifting a 1 bit left 100 places.
	// In other words, the binary number that is 1 followed by 100 zeroes.
	Big = 1 << 100
	// Shift it right again 99 places, so we end up with 1<<1, or 2.
	Small = Big >> 99
)
func needInt(x int) int { return x*10 + 1 }
func needFloat(x float64) float64 {
	return x * 0.1
}

func numericConstants() {
	fmt.Println(" ")
	fmt.Println("16.NumericConstants")
	fmt.Println(needInt(Small))
	fmt.Println(needFloat(Small))
	fmt.Println(needFloat(Big))
}