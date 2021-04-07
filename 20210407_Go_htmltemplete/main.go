package main

import (
	"html/template"
	"log"
	"net/http"
)

type ProductItem struct {
	Name     string
	Price    int
	Discount int
}

func (p *ProductItem) NewPrice() int {
	return p.Price - p.Discount
}

func handler(w http.ResponseWriter, r *http.Request) {

	tl := template.Must(template.ParseFiles("index.html"))

	data := map[string]interface{}{}
	products := []ProductItem{
		{Name: "banana", Price: 110, Discount: 0},
		{Name: "apple", Price: 150, Discount: 25},
		{Name: "grape", Price: 250, Discount: 50},
		{Name: "strawberry", Price: 300, Discount: 170},
	}
	data["products"] = products

	if err := tl.Execute(w, data); err != nil {
		log.Fatal(err)
	}
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8888", nil)
}
