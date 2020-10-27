def zad41(data):
    result = str("")
    for i in range(39, len(data), 40):
        result += str(data[i])[9]
    return result

def zad42(data):
    class Result:
        def __init__(self):
            self.word = None
            self.counter = 0

        def __str__(self):
            return f'{self.word, self.counter}'


    class Alfabet:
        def __init__(self):
            self.alfabet = {
                "a": 0,
                "b": 0,
                "c": 0,
                "d": 0,
                "e": 0,
                "f": 0,
                "g": 0,
                "h": 0,
                "i": 0,
                "j": 0,
                "k": 0,
                "l": 0,
                "m": 0,
                "n": 0,
                "o": 0,
                "p": 0,
                "q": 0,
                "r": 0,
                "s": 0,
                "t": 0,
                "u": 0,
                "v": 0,
                "w": 0,
                "x": 0,
                "y": 0,
                "z": 0
            }

        def add(self, char):
            self.alfabet[str(char).lower()] += 1

        def count(self):
            counter = 0
            for i in range(ord("a"),ord("z")+1,1):
                if self.alfabet[chr(i)] != 0:
                    counter += 1
            return counter
                
        def __str__(self):
            return f'{self.alfabet}'
    
    result = Result()

    for i in range(len(data)):
        alfabet = Alfabet()
        for j in range(len(data[i])):
            alfabet.add(data[i][j])
        if alfabet.count() > result.counter:
            result.word = data[i]
            result.counter = alfabet.count()

    return result



def zad43(data):
    def wordCheck(word):
        for i in range(1,len(word),1):
            if abs(ord(word[i-1])-ord(word[i])) > 10:
                return False
        return True
    result = list()
    for i in range(len(data)):
        if wordCheck(data[i]):
            result.append(data[i])
    return result

def main():
    przyklad = "/home/jakub/C/School/ZSK-4D/zsk-informatyka/src/lessons/lesson3/data/informatyka-2018-maj-matura-rozszerzona-zalaczniki/Dane_PR/przyklad.txt"
    path = "/home/jakub/C/School/ZSK-4D/zsk-informatyka/src/lessons/lesson3/data/informatyka-2018-maj-matura-rozszerzona-zalaczniki/Dane_PR/sygnaly.txt"
    data = open(path, "r", encoding="utf-8").read().splitlines()
    
    res1 = zad41(data)
    res2 = zad42(data)
    res3 = zad43(data)

    print("Zadanie 4.1:", res1)
    print("Zadanie 4.2:", res2)
    print("Zadanie 4.3:")

    for i in range(len(res3)):
        print(res3[i])


if __name__ == "__main__":
    main()