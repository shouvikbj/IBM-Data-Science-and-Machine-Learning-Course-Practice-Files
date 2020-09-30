def fun1():
    print("fun1() called.")


def fun2(name):
    fun1()
    print(f"Hi {name}")
    fun1()


fun1()
fun2("Shouvik")


# addition function for any number of inputs
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


result1 = add(1, 2, 3, 4)
print(result1)
result2 = add(5, 8)
print(result2)