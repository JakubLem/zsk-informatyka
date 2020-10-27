# punkty xy - egzamin maturalny - czerwiec 2017


class Punkt:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'{self.x, self.y}'

def zad1(points):
    pass

def main():
    data = open("D:/School/zsk-informatyka/src/lessons/lesson5/MIN-DANE-2017/punkty.txt", "r", encoding="utf-8").read().splitlines()
    points = list()
    for i in range(len(data)):
        row = data[i].split()
        points.append(Punkt(row[0], row[1]))



if __name__ == "__main__":
    main()
