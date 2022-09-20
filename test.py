# This is my first script

def test_memory():
    L=[1,2,3,4]
    for i in L:
        print(hex(id(i)))
    print("Change affectation")
    L[1] = 10
    for i in L:
        print(hex(id(i)))


def test_memory_primitives():
    print("primitives")
    a = 1
    print(hex(id(a)))
    print(hex(id(1)))
    print(hex(id(2)))
    print(hex(id(3)))
    print("list")
    b = []
    print(hex(id([])))
    print(hex(id(b)))

def my_filter(func, seq):
    res = []
    for el in seq:
        if func(el):
            res.append(el)
    return res


def Fibonacci():
    a, b, c = 1, 1, 1
    while c < 15:
        a, b, c = b, a + b, c + 1
        print(b)


print(my_filter(lambda x:len(x)>3, [[1,2,3,4,5,6],[5,6]]))