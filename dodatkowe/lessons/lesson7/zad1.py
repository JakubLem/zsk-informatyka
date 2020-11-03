# Tworzenie algorytmów	Podobne tablice	Egzamin maturalny — czerwiec 2020
# Zadanie 1.2.

def czy_k_podobne(n, A, B, k):
    for i in range(n-k-1):
        if A[i] != B[i+k+1]:
            return False
    for i in range(k):
        if A[i+k] != B[i]:
            return False
    return True

"""
A = (4,7,1,4,5)
B = (1,4,5,4,7)

n = 5
k = 2
"""
A = [10, 9, 12, 10, 9]
B = [10, 10, 9, 9, 12]

n = 5
k = 3



print(czy_k_podobne(n, A, B, k))
