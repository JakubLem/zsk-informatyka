

def zad1(liczby):
    # TODO
    pass




def main():
    liczby = open("src/lessons/lesson4/czerwier2016/MIN-R2A1P-163_dane/liczby.txt", "r", encoding="utf-8").read().splitlines()

    print("zad1", zad1(liczby))
    """print("zad2", zad2(liczby))
    print("zad3", zad3(liczby))"""


if __name__ == "__main__":
    main()