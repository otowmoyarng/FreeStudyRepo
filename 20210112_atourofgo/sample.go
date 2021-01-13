package main

import (
	"fmt"
	"math"
	"math/rand"
	"math/cmplx"
	"runtime"
	"time"
)

func main() {
	fmt.Println("a Tour of Go 開始")
	/* basics */
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

	/* flowcontrol */
	for1()
	for2()
	gowhile()
	//forever()
	if1()
	if2()
	ifelse()
	switch1()
	switch2()
	switch3()
	defer1()
	defer2()

	fmt.Println(" ")
	fmt.Println("a Tour of Go 終了")
}

/* basics */
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
	const World string = "世界"
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

/* flowcontrol */
func for1() {
	fmt.Println(" ")
	fmt.Println("1.for1")
	sum := 0
	for i = 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}

func for2() {
	fmt.Println(" ")
	fmt.Println("2.for2")
	sum := 1
	for ; sum < 1000; {
		sum += sum
	}
	fmt.Println(sum)
}

func gowhile() {
	fmt.Println(" ")
	fmt.Println("3.gowhile")
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}

func forever() {
	fmt.Println(" ")
	fmt.Println("4.forever()")
	for {

	}
}

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func if1() {
	fmt.Println(" ")
	fmt.Println("5.if1")
	fmt.Println(sqrt(2), sqrt(-4))
}

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	return lim
}
func if2() {
	fmt.Println(" ")
	fmt.Println("6.if2")
	fmt.Println(pow(3, 2, 10), pow(3, 3, 10))
}

func ifelse() {
	fmt.Println(" ")
	fmt.Println("7.ifelse")
	fmt.Println(pow(3, 2, 10), pow(3, 3, 10))
}

func switch1() {
	fmt.Println(" ")
	fmt.Println("8.switch1")
	switch os := runtime.GOOS; os {
		case "darwin":
			fmt.Println("OS X.")
		case "linux":
			fmt.Println("Linux.")
		default:
			fmt.Printf("%s.\n", os)
	}
}

func switch2() {
	fmt.Println(" ")
	fmt.Println("9.switch2")
	fmt.Println("When's Saturday?")
	today := time.Now().Weekday()
	switch time.Saturday {
		case today + 0:
			fmt.Println("Today.")
		case today + 1:
			fmt.Println("Tomorrow.")
		case today + 2:
			fmt.Println("In two days.")
		default:
			fmt.Println("Too far away.")
	}
}

func switch3() {
	fmt.Println(" ")
	fmt.Println("10.switch3")
	t := time.Now()
	switch {
		case t.Hour() < 12:
			fmt.Println("Good morning!")
		case t.Hour() < 17:
			fmt.Println("Good afternoon.")
		default:
			fmt.Println("Good evening.")
	}
}

func defer1() {
	fmt.Println(" ")
	fmt.Println("11.defer1")

	defer fmt.Println("test")
	defer fmt.Println("world")
	fmt.Println("hello")
}

func defer2() {
	fmt.Println(" ")
	fmt.Println("12.defer2")

	fmt.Println("counting")
	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("done")
}