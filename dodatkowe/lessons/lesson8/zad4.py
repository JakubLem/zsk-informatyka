PATH = "/home/jakub/C/School/ZSK-4D/zsk-informatyka/dodatkowe/lessons/lesson8/data/informatyka-2020-czerwiec-matura-rozszerzona-zalaczniki/Dane_PR2/pary.txt"


class Row:
    def __init__(self, number, string):
        self.number = int(number)
        self.string = string

    def __str__(self):
        return f'{self.number, self.string}'

def ex1(rows):
    

def main():
    data = open(PATH, "r", encoding="utf-8").read().splitlines()
    rows = list()
    for i in range(len(data)):
        rows.append(Row(data[i].split()[0], data[i].split()[1]))

    
    res_ex1 = ex1(rows)



if __name__ == "__main__":
    main()