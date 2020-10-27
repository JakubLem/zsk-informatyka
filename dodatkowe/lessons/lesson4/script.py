def fun(n):
    if n == 1 or n == 2:
        s = n
    else:
        s = n*fun(n-2)
    return s*(n+1)


# Ulubione liczby


def ulubione(tab,n):
    p = 1
    q = n
    while p < q:
        s = int((p+q)/2)
        if tab[s] % 2 == 0:
            q = s
        else:
            p = s + 1
    w = tab[p]
    return w

tab = [5,99,3,7,111,15,4,24,8]
n = len(tab)

print(ulubione(tab,n))