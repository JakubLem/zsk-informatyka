# Analiza algorytmu - Egzamin maturalny - maj 2019

"""

Przeanalizuj podaną funkcję pisz.
Specyfikacja:
Dane:
s – napis
n – liczba całkowita dodatnia, nie mniejsza niż długość napisu s
k – liczba całkowita z zakresu [2..10]
funkcja pisz(s,n,k)
 jeżeli dł(s) = n
wypisz s
w przeciwnym razie
 dla i=0,1 … k-1 wykonuj
pisz(s + napis(i), n, k)

Uwaga:
dł(x) – daje w wyniku długość napisu x
s1 + s2 – daje w wyniku złączenie napisów s1 i s2
napis(p) – daje w wyniku napis będący zapisem dziesiętnym liczby całkowitej p 

"""

def pisz(s, n, k):
    print("xd")
    if len(s) == n:
        print(s)
    else:
        for i in range(0, k, 1):
            pisz(s+str(i), n, k)

pisz("",2,3)

# Zadanie 2.2 

# pisz("",3,2)  000 001 010 011 100 101 110 111 Liczba wywołań 8

# pisz("",2,3)  00  01  02  10  11  12  20  21  22  Liczba wywołań 13