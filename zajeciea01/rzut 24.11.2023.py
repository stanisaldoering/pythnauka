# gracz zaczyna z 100 punktami gra polega na 3 kolejnych rzutach ksocia kazdy kolejny rzut zmienia ilosc punktow gracza wedlug ponizszego schemati
# wypadła 6 punkty pozostaja bez zmain, wypadaa 5 lub 4 punkty gracza mnozymy x2
# wypadla 3 lub 2 dzielimy 2 porzucamy czesc dziesietna
# wypadla 1 gracz traci wszystkie punty  oprocz 1
# zaimplemetnuj wynik 1 rzutu koscia funkcja rzut, napisz funkcje ktora ma przyjmowac punkty i wyniki rzutow
# a zwaracac liczbe punktow jaka otrzyma gracz na koniec gry
from random import randint
def los(n):
    lista = []
    for i in range(n):
        lista.append(randint(1,6))
    return lista


def rzut(punkty, rzut_kostka):
    if rzut_kostka == 6:
        return punkty
    if rzut_kostka in (5,4):
        return punkty * 2
    if rzut_kostka == 3 or rzut_kostka == 2:
        return punkty//2
    if rzut_kostka == 1:
        return 1



def rezultat(punkty, tab):
    for i in tab:
        punkty = rzut(punkty, i)
    return punkty

tab = los(3)
print(tab)
print(rezultat(100, tab))
