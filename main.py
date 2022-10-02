def fib_recursive(x):
    if x == 0:
        return 0
    if x <= 2:
        return 1
    return fib_recursive(x - 1) + fib_recursive(x - 2)


def fib_iterative(x):
    a = 0
    b = 1
    if x == 0:
        return a
    for j in range(x):
        c = b
        b = a
        a = b + c
    return a


if __name__ == '__main__':
    print("Recursive:")
    for i in range(10):
        print(fib_recursive(i))
    print("Iterative:")
    for i in range(10):
        print(fib_iterative(i))
