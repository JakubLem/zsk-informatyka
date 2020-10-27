def ownSQRT(a):
    p = 1
    q = a + 1
    safeiter = 0
    while ((p+q)/2)*((p+q)/2) != a:
        q = (p+q)/2
        safeiter += 1
        if safeiter == 1000:
            return "ERROR"
    return (p+q)/2

print(ownSQRT(25))
