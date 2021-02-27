package main

import (
	"fmt"
	"net/http"
)

type Index3 string

func (s Index3) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	fmt.Fprint(res, s)
}

func main() {
	http.HandleFunc("/index1", index1)
	http.HandleFunc("/index2", func(res http.ResponseWriter, req *http.Request) {
		fmt.Fprint(res, "Hello http Go requested index2")
	})
	http.Handle("/index3", Index3("Hello http Go requested index3"))

	http.ListenAndServe(":8080", nil)
}

func index1(res http.ResponseWriter, req *http.Request) {
	fmt.Fprint(res, "Hello http Go requested index1")
}
