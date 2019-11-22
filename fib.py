def fib():
    a = 0
    b = 0
    c = 0
    fibs = [1, 2]
    for i in range(1,99):
        a = fibs[len(fibs)-1]
        b = fibs[len(fibs)-2]
        c = a + b
        fibs.append(c)
    return fibs
