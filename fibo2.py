

def fibo2():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == '__main__':

    fib = fibo2()
    for i in range(10):
        print(next(fib), end=' ')
