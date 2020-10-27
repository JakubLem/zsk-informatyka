# 2020 kwiecień

def zad1(liczby):
    maxim = abs(liczby[0]-liczby[1])
    minim = abs(liczby[0]-liczby[1])
    for i in range(1, len(liczby)-1, 1):
        if abs(liczby[i]-liczby[i+1]) > maxim:
            maxim = abs(liczby[i]-liczby[i+1])
        elif abs(liczby[i]-liczby[i+1]) < minim:
            minim = abs(liczby[i]-liczby[i+1])
    return {"minim": minim, "maxim": maxim}

"""ŹLE"""
"""
def zad2(liczby):
    result = None
    max_len = 0
    for i in range(len(liczby)):
        x = str(liczby[i])
        checker = True
        firstAbs = abs(int(x[0])-int(x[1]))
        for y in range(len(x)-1):
            if abs(int(x[y])-int(x[y+1])) != firstAbs:
                checker = False
                continue
        if checker:
            if len(x) > max_len:
                result = x
                max_len = len(x)
    return {"result": result, "max_len": max_len}
"""

def zad2(liczby):
    pass

def main():
    path = "/home/jakub/C/School/ZSK-4D/zsk-informatyka/dodatkowe/lessons/lesson6/informatyka-2020-kwiecien-probna-rozszerzona-zalaczniki/dane4.txt"
    data = open(path, "r", encoding="utf-8").read().splitlines()
    liczby = list()
    for i in range(len(data)):
        liczby.append(int(data[i]))
    print(zad1(liczby))
    print(zad2(liczby))

if __name__ == "__main__":
    main()