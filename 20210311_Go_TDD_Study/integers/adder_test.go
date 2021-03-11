package integers

import "testing"

func TestAdd(t *testing.T) {

	sum := Add(1, 2)
	expect := 3
	if sum != expect {
		t.Errorf("sum %d expect %d", sum, expect)
	}
}
