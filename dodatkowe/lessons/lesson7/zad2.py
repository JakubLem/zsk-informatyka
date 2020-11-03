# Tworzenie algorytmów	Liczby Fibonacciego	Egzamin maturalny — czerwiec 2018
# Zad1



def fib(n):
    n = int(n)
    a = 1
    b = 1
    for i in range(2, n, 1):
        c = a + b
        a = b
        b = c
    return b

print(fib(5))


# 1 1 2 3 5

# TODO
def f(n):
    if n % 2 == 0:
        return pow(fib((n/2)+1), 2) - pow(f((n/2)-1), 2)
    else:
        return pow(fib((n+1)/2), 2) + pow(f(((n+1)/2)-1), 2)

print(f(5))