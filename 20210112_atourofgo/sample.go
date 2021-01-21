package main

import (
	"fmt"
	"image"
	"io"
	"math"
	"math/cmplx"
	"math/rand"
	"runtime"
	"strings"
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
	switch4()
	defer1()
	defer2()

	/* moretypes */
	pointers()
	structs1()
	structs2()
	structs3()
	array1()
	slice1()
	slice2()
	slice3()
	slice4()
	slice5()
	slice6()
	slice7()
	slice8()
	slice9()
	range1()
	range2()
	map1()
	map2()
	map3()
	map4()
	functionvalues1()
	functionvalues2()

	/* Methods and Interfaces */
	methods1()
	methods2()
	methods3()
	methods4()
	methods5()
	methods6()
	methods7()
	methods8()
	methods9()
	methods10()
	interfaces1()
	interfaces2()
	interfaces3()
	interfaces4()
	interfaces5()
	interfaces6()
	typeassertions()
	typeswitch()
	stringer1()
	stringer2()
	error1()
	readers1()
	images1()

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
	for sum < 1000 {
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

func switch4() {
	fmt.Println(" ")
	fmt.Println("11.switch4")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow.")
	case today + 2:
		fmt.Println("In two days.")
		fallthrough
	default:
		fmt.Println("Too far away.")
	}
}

func defer1() {
	fmt.Println(" ")
	fmt.Println("12.defer1")

	defer fmt.Println("test")
	defer fmt.Println("world")
	fmt.Println("hello")
}

func defer2() {
	fmt.Println(" ")
	fmt.Println("13.defer2")

	fmt.Println("counting")
	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("done")
}

/* moretypes */
func pointers() {
	fmt.Println(" ")
	fmt.Println("1.pointers")
	i, j := 42, 2701

	p := &i
	fmt.Println("p:", *p)
	*p = 21
	fmt.Println("i:", i)
	fmt.Println("p:", *p)

	p = &j
	*p = *p / 37
	fmt.Println("j:", j)
	fmt.Println("p:", *p)
}

type Vertex struct {
	X, Y int
}

func structs1() {
	fmt.Println(" ")
	fmt.Println("2.structs1")
	fmt.Println(Vertex{1, 2})
}

func structs2() {
	fmt.Println(" ")
	fmt.Println("3.structs2")
	var v Vertex = Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}

var (
	v1 = Vertex{1, 2}
	v2 = Vertex{X: 1}
	v3 = Vertex{}
	p  = &Vertex{1, 2}
)

func structs3() {
	fmt.Println(" ")
	fmt.Println("4.structs3")
	fmt.Println(v1, v2, v3, p)
}

func array1() {
	fmt.Println(" ")
	fmt.Println("5.array1")
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)
}

func slice1() {
	fmt.Println(" ")
	fmt.Println("6.slice1")
	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)

	var s []int = primes[1:4]
	fmt.Println(s)
}

func slice2() {
	fmt.Println(" ")
	fmt.Println("7.slice2")
	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println(names)

	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)
}

func slice3() {
	fmt.Println(" ")
	fmt.Println("8.slice3")
	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(q)

	r := []bool{true, false, true, true, false, true}
	fmt.Println(r)

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)
}

func slice4() {
	fmt.Println(" ")
	fmt.Println("9.slice4")
	s := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(s)

	t := s[1:4]
	fmt.Println(t)

	t = s[:2]
	fmt.Println(t)

	t = s[1:]
	fmt.Println(t)

	t = s[:]
	fmt.Println(t)
}

func slice5() {
	fmt.Println(" ")
	fmt.Println("10.slice5")
	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	s = s[:0]
	printSlice(s)

	s = s[:4]
	printSlice(s)

	s = s[2:]
	printSlice(s)
}
func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func slice6() {
	fmt.Println(" ")
	fmt.Println("11.slice6")
	var s []int
	fmt.Println(s, len(s), cap(s))
	if s == nil {
		fmt.Println("nil!")
	}
}

func slice7() {
	fmt.Println(" ")
	fmt.Println("12.slice7")

	a := make([]int, 5)
	printSlice2("a", a)

	b := make([]int, 0, 5)
	printSlice2("b", b)

	c := b[:2]
	printSlice2("c", c)

	d := c[2:5]
	printSlice2("d", d)
}
func printSlice2(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}

func slice8() {
	fmt.Println(" ")
	fmt.Println("13.slice8")

	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}

func slice9() {
	fmt.Println(" ")
	fmt.Println("14.slice9")

	var s []int
	printSlice3(s)

	s = append(s, 0)
	printSlice3(s)

	s = append(s, 1)
	printSlice3(s)

	s = append(s, 2, 3, 4)
	printSlice(s)
}
func printSlice3(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func range1() {
	fmt.Println(" ")
	fmt.Println("15.range1")
	var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}

func range2() {
	fmt.Println(" ")
	fmt.Println("16.range2")
	pow := make([]int, 10)
	for i := range pow {
		pow[i] = 1 << uint(1)
	}
	for _, value := range pow {
		fmt.Printf("%d\n", value)
	}
}

type VertexA struct {
	Lat, Long float64
}

func map1() {
	fmt.Println(" ")
	fmt.Println("17.map1")
	var m map[string]VertexA = make(map[string]VertexA)
	m["Bell Labs"] = VertexA{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
}

func map2() {
	fmt.Println(" ")
	fmt.Println("18.map2")
	var m = map[string]VertexA{
		"Bell Labs": VertexA{
			40.68433, -74.39967,
		},
		"Google": VertexA{
			37.42202, -122.08408,
		},
	}
	fmt.Println(m)
}

func map3() {
	fmt.Println(" ")
	fmt.Println("19.map3")
	var m = map[string]VertexA{
		"Bell Labs": {
			40.68433, -74.39967,
		},
		"Google": {
			37.42202, -122.08408,
		},
	}
	fmt.Println(m)
}

func map4() {
	fmt.Println(" ")
	fmt.Println("20.map4")
	var m = make(map[string]int)

	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)

	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])

	v, ok = m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}

func functionvalues1() {
	fmt.Println(" ")
	fmt.Println("21.functionvalues1")

	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*y + y*x)
	}
	fmt.Println(hypot(5, 12))
	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func functionvalues2() {
	fmt.Println(" ")
	fmt.Println("22.functionvalues2")

	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(i, pos(i), neg(-2*i))
	}
}
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

type Vertex2 struct {
	X, Y float64
}

func (v Vertex2) Abs1() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
func methods1() {
	fmt.Println(" ")
	fmt.Println("1.methods1")

	v := Vertex2{3, 4}
	fmt.Println(v.Abs1())
}

func Abs2(v Vertex2) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
func methods2() {
	fmt.Println(" ")
	fmt.Println("2.methods2")

	v := Vertex2{3, 4}
	fmt.Println(Abs2(v))
}

type MyFloat float64

func (f MyFloat) Abs3() float64 {
	if f < 0 {
		return float64(f)
	}
	return float64(f)
}
func methods3() {
	fmt.Println(" ")
	fmt.Println("3.methods3")

	f := MyFloat(-math.Sqrt2)
	fmt.Println(f.Abs3())
}

func (v Vertex2) Scale1(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
func methods4() {
	fmt.Println(" ")
	fmt.Println("4.methods4")

	v := Vertex2{3, 4}
	v.Scale1(10)
	fmt.Println(v.Abs1())
}

func (v *Vertex2) Scale2(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
func methods5() {
	fmt.Println(" ")
	fmt.Println("5.methods5")

	v := Vertex2{3, 4}
	v.Scale2(10)
	fmt.Println(v.Abs1())
}

func Scale3(v *Vertex2, f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
func methods6() {
	fmt.Println(" ")
	fmt.Println("6.methods6")

	v := Vertex2{3, 4}
	Scale3(&v, 10)
	fmt.Println(Abs2(v))
}

func Scale4(v Vertex2, f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
func methods7() {
	fmt.Println(" ")
	fmt.Println("7.methods7")

	v := Vertex2{3, 4}
	Scale4(v, 10)
	fmt.Println(Abs2(v))
}

func (v *Vertex2) Scale5(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
func ScaleFunc(v *Vertex2, f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
func methods8() {
	fmt.Println(" ")
	fmt.Println("8.methods8")

	v := Vertex2{3, 4}
	v.Scale5(2)
	ScaleFunc(&v, 10)

	p := &Vertex2{4, 3}
	p.Scale5(3)
	ScaleFunc(p, 8)

	fmt.Println(v, p)
}

func (v Vertex2) Abs3() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
func Absfunc(v Vertex2) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
func methods9() {
	fmt.Println(" ")
	fmt.Println("9.methods9")

	v := Vertex2{3, 4}
	fmt.Println(v.Abs3())
	fmt.Println(Absfunc(v))

	p := &Vertex2{3, 4}
	fmt.Println(p.Abs3())
	fmt.Println(Absfunc(*p))
}

func (v *Vertex2) Scale6(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
func (v *Vertex2) Abs4() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
func methods10() {
	fmt.Println(" ")
	fmt.Println("10.methods10")

	v := &Vertex2{3, 4}
	fmt.Printf("Before scaling: %+v, Abs: %v\n", v, v.Abs4())
	v.Scale6(5)
	fmt.Printf("After scaling: %+v, Abs: %v\n", v, v.Abs4())
}

type Abser interface {
	Abs() float64
}

func interfaces1() {
	fmt.Println(" ")
	fmt.Println("11.interfaces1")

	var a Abser
	f := MyFloat(-math.Sqrt2)
	v := Vertex2{3, 4}
	// a = f
	// a = &v
	fmt.Println(f)
	fmt.Println(v)
	fmt.Println(a)
	// fmt.Println(a.Abs())	ランタイムエラーとなる
}

type I1 interface {
	M1()
}

type T struct {
	S string
}

func (t T) M1() {
	fmt.Println(t.S)
}
func interfaces2() {
	fmt.Println(" ")
	fmt.Println("12.interfaces2")

	var i I1 = T{"Hello"}
	i.M1()
}

type I2 interface {
	M2()
}
type F float64

func (t *T) M2() {
	fmt.Println(t.S)
}
func (f F) M2() {
	fmt.Println(f)
}
func interfaces3() {
	fmt.Println(" ")
	fmt.Println("13.interfaces3")

	var i I2
	i = &T{"Hello"}
	describe1(i)
	i.M2()

	i = F(math.Pi)
	describe1(i)
	i.M2()
}
func describe1(i I2) {
	fmt.Printf("(%v, %T)\n", i, i)
}

type I3 interface {
	M3()
}

func (t *T) M3() {
	if t == nil {
		fmt.Println("<nil>")
		return
	}
	fmt.Println(t.S)
}
func interfaces4() {
	fmt.Println(" ")
	fmt.Println("14.interfaces4")

	var i I3
	var t *T
	i = t
	describe2(i)
	i.M3()

	i = &T{"Hello"}
	describe2(i)
	i.M3()
}
func describe2(i I3) {
	fmt.Printf("(%v, %T)\n", i, i)
}

type I4 interface {
	M4()
}

func interfaces5() {
	fmt.Println(" ")
	fmt.Println("15.interfaces5")

	var i I4
	describe3(i)
	// i.M4()	ランタイムエラーとなる
}
func describe3(i I4) {
	fmt.Printf("(%v, %T)\n", i, i)
}

func interfaces6() {
	fmt.Println(" ")
	fmt.Println("16.interfaces6")

	var i interface{}
	describe4(i)

	i = 42
	describe4(i)

	i = "Hello"
	describe4(i)
}
func describe4(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}

func typeassertions() {
	fmt.Println(" ")
	fmt.Println("17.typeassertions")

	var i interface{} = "hello"

	s := i.(string)
	fmt.Println(s)

	s, ok := i.(string)
	fmt.Println(s, ok)

	f, ok := i.(float64)
	fmt.Println(f, ok)

	// f = i.(float64) // panic
	// fmt.Println(f)
}

func do(i interface{}) {
	switch v := i.(type) {
	case int:
		fmt.Printf("Twice %v is %v\n", v, v*2)
	case string:
		fmt.Printf("%q is %v bytes long\n", v, len(v))
	default:
		fmt.Printf("I don't know about type %T!\n", v)
	}
}
func typeswitch() {
	fmt.Println(" ")
	fmt.Println("18.typeswitch")

	do(21)
	do("hello")
	do(true)
}

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}
func stringer1() {
	fmt.Println(" ")
	fmt.Println("19.stringer1")

	a := Person{"Arthur Dent", 42}
	z := Person{"Zaphod Beeblebrox", 9001}
	fmt.Println(a, z)
}

type IPAddr [4]byte

func stringer2() {
	fmt.Println(" ")
	fmt.Println("20.stringer2")
	hosts := map[string]IPAddr{
		"loopback":  {127, 0, 0, 1},
		"googleDNS": {8, 8, 8, 8},
	}
	for name, ip := range hosts {
		fmt.Printf("%v: %v\n", name, ip)
	}
}

type MyError struct {
	When time.Time
	What string
}

func (e *MyError) Error() string {
	return fmt.Sprintf("at %v, %s", e.When, e.What)
}

func run() error {
	return &MyError{time.Now(), "it didn't work"}
}
func error1() {
	fmt.Println(" ")
	fmt.Println("21.error1")

	if err := run(); err != nil {
		fmt.Println(err)
	}
}

func readers1() {
	fmt.Println(" ")
	fmt.Println("22.readers1")

	r := strings.NewReader("Hello, Reader!")
	b := make([]byte, 8)
	for {
		n, err := r.Read(b)
		fmt.Printf("n = %v err = %v b = %v\n", n, err, b)
		fmt.Printf("b[:n] = %q\n", b[:n])
		if err == io.EOF {
			break
		}
	}
}

func images1() {
	fmt.Println(" ")
	fmt.Println("23.image1")

	m := image.NewRGBA(image.Rect(0, 0, 100, 100))
	fmt.Println(m.Bounds())
	fmt.Println(m.At(0, 0).RGBA())
}
