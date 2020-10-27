# Egzamin maturalny - maj 2017 - Tworzenie prostokątów
def zad_1_2(n,a,p):
    x = 0
    y = 0
    for i in range(n):
        if a[i]%p != 0:
            if a[i] > x:
                y = x
                x = a[i]
            elif a[i] > y:
                y = a[i]
    print(x, y)

# Egzamin maturalny - czerwiec 2015 - Triady
def zad_2_2(n,c):
    counter = 0
    for i in range(n):
        if c[0] + c[1] < c[i] and c[1]-c[0] > c[i]:
            counter += 1
    print(counter)





zad_1_2(5, [5,4,3,2,5],3)
zad_2_2(5, [1,2,3,4,5])
