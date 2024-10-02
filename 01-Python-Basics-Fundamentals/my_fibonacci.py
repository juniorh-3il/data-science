def fib(n):
    a = 0
    b = 1
    for i in range(n-1):
        print(a),
        a, b = b, a+b

def fib_list(n=10):
    a = 0
    b = 1
    res = []
    for i in range(n-1):
        res.append(a)
        a, b = b, a+b
    return res