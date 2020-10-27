def zad1(liczby):
    result = 0
    for i in range(len(liczby)):
        liczba = liczby[i]
        counter = 0
        for x in range(len(str(liczba))):
            if int(liczba[x]) == 0:
                counter += 1
        if counter > len(liczba)/2:
            result += 1
    return result


def zad2(liczby):
    # TODO dodać ord()
    counter_2 = 0
    counter_8 = 0
    for i in range(len(liczby)):
        liczba = liczby[i]
        if int(liczba[len(liczba)-1]) == 0:
            counter_2 += 1
        if int(liczba[len(liczba)-1]) == 0 and int(liczba[len(liczba)-2]) == 0 and int(liczba[len(liczba)-3]) == 0:
            counter_8 += 1
    return {"2": counter_2, "8": counter_8}

def zad3(liczby):
    maximum = 0
    minimum = 0
    for i in range(1, len(liczby), 1):
        liczba = liczby[i]
        if len(liczba) <= len(liczby[minimum]):
            if len(liczba) < len(liczby[minimum]):
                minimum = i
            else:
                for x in range(len(liczba)):
                    if int(liczba[x]) == 0 and int(str(liczby[minimum])[x]) == 1:
                        minimum = i
                        continue
        elif len(liczba) >= len(liczby[maximum]):
            if len(liczba) > len(liczby[maximum]):
                maximum = i
            else:
                for x in range(len(liczba)):
                    if int(liczba[x]) == 1 and int(str(liczby[maximum])[x]) == 0:
                        maximum = i
                        continue
    return {"min": minimum + 1, "max": maximum + 1}





def main():
    liczby = open("src/lessons/lesson4/Dane_PR/liczby.txt", "r", encoding="utf-8").read().splitlines()
    print("zad1", zad1(liczby))
    print("zad2", zad2(liczby))
    print("zad3", zad3(liczby)) # TODO

if __name__ == "__main__":
    main()