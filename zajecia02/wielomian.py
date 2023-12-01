# napisz program ktory obliczy wartosc wielomianu algorytem naiwnym  wykorzystujacy funkcje pobierania argumentu o podanym stopniu wielomianu
x=int(input("podaj x"))
s = int(input("podaj stopien wielomianu"))
def stopien(s):
    stopnie=[]
    for i in range(0,s+1):
        stopnie.append(i)
    return stopnie
print(stopien(s))

