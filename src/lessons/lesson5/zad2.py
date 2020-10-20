# Krajobraz - Egzamin maturalny - maj 2018


"""

W pewnym paśmie górskim znajduje się n szczytów, które będziemy przedstawiać jako punkty
w układzie kartezjańskim na płaszczyźnie. Wszystkie punkty leżą powyżej osi OX, tzn. druga
współrzędna (y) każdego punktu jest dodatnia.
W punkcie (0,0) stoi obserwator. Jeśli dwa szczyty A i B mają współrzędne (xA, yA) oraz
(xB, yB), to mówimy, że:
• szczyt A jest dla obserwatora widoczny na lewo od B, jeśli xA/yA < xB/yB;
• szczyt B jest widoczny na lewo od A, jeśli xA/yA > xB/yB.
Wiemy, że żadne dwa szczyty nie leżą w jednej linii z obserwatorem, a zatem dla obserwatora
te szczyty nie zasłaniają się nawzajem. Ilustrację przykładowego położenia szczytów można
zobaczyć na poniższym rysunku: 

W tym przykładzie, patrząc od lewej do prawej strony, obserwator widzi kolejno szczyt D,
szczyt A, szczyt B i szczyt C.
Współrzędne szczytów dane są w dwóch tablicach X[1..n] oraz Y[1..n] – szczyt numer i ma
współrzędne (X[i], Y[i]).

"""


"""class Szczyt:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.name, self.x, self.y}'

    def value(self):
        return round(self.x/self.y,2)



szczyty = list()
szczyty.append(Szczyt('A',1,3))
szczyty.append(Szczyt('B',3,4))
szczyty.append(Szczyt('C',2,1))
szczyty.append(Szczyt('D',-2,2))

for i in szczyty:
    print(i)
    print(i.value())"""

def zad21(n, x, y):
    first = 0
    first_value = x[0]/y[0]
    for i in range(1, n, 1):
        if x[i]/y[i] < first_value:
            first = i
            first_value = x[i]/y[i]
    return first

def zad22(n, x, y):
    for i in range(1, n, 1):
        kx = x[i]
        ky  = y[i]
        j = i - 1
        while j > -1 and x[j]/y[j] > k:
            x[j + 1] = x[j]
            y[j + 1] = y[j]
            j  -= 1
        x[j + 1]  # TODO

def main():
    n = 5
    x = (9, 7, -1, -2, 5)
    y = (10, 7, 10, 1, 8)
    print(zad21(n, x, y))


if __name__ == "__main__":
    main()
