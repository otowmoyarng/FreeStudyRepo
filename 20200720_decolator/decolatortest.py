# 引数なし
def deco1(func):
    def decoinnerfunc1(func):
        print("decoinnerfunc1:start")
        func()
        print("decoinnerfunc1:end")
    return decoinnerfunc1(func)

# 引数あり
def deco2(num):
    def decoinnerfunc2(func):
        print("decoinnerfunc2:start")
        print("args:" + num)
        func()
        print("decoinnerfunc2:end")
    return decoinnerfunc2

@deco1
def decotest1():
    print("decotest1")

@deco2("2")
def decotest2():
    print("decotest2")

# decotest1()
# decotest2()
