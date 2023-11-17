import math
import math
a = 0.0001
b = 150
c = 5
delta = b*b - 4*a*c

if delta>0:
    pierwdelta = math.sqrt(delta)
    x1 = -b-pierwdelta//2*a
    x2 = -b+pierwdelta//2*a
    print(delta,x1,x2)
if delta == 0:
    x0 = -b//2*a
    print(x0)
if delta<0:
    print("brak pierwiastkow kwadratowych")


# napisz program podajacy wynik obliczenia zamiany ułamaka binarengo na liczbe dziesietna przy zamianaie podajemy ilosc bitow
# na jakich jest zapisana podana liczba
def binFloat(n):
    wynik=0
    for i in range(2,len(n)):
        wynik+=2**(-i-1)
    return(wynik)
print(binFloat("0,101"))