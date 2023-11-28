# def binFloat(n,ilebit=0):
#     wynik=0
#     for i in range(2,ilebit+2):
#         if n[i]=="1" or n[i]=='0':
#             if n[i]=='1':
#                 wynik+=2**(-i+1)
#         else:
#             return 'error'
#     return(wynik)
#
# print(binFloat("0,00011001100110011",8))
# x=0.1
# y1=(binFloat("0,00011001100110011",8))
# y2=(binFloat("0,00011001100110011",12))
# y3=(binFloat("0,00011001100110011",16))
#
# print("y1",x-y1)
# print("y2",x-y2)
# print("y3",x-y3)
# wratosc dokladna x=0,1 w systemie dziesietny jest rowna 0,1 oblicz jaki bedzie blad przy zapisie liczby 0,1 z wykorzytsaniem 8 bit,12, 16

# napisz program  ktroy obliczby  wartosc sinusa 1 korzystajac ze wzoru sin
# obliczenia wykonaj z dokladnoscia do 4 liczb

# skladowa=1
# i=1
# wynik=0
# while skladowa>eps:
#     i+=2
#     wynik+=skladowa/i
#     skladowa /=i
#     print(skladowa)
#
def silnia(n):
    w=1
    for i in range(1,n+1):
        w*=i
    return w
print(silnia(4))
def zadanie():
    eps=0.0001
    wynik=1.0
    k=3
    skladnik=1/silnia(3)
    znak=-1
    while skladnik>=eps:
        wynik+=znak *skladnik
        k+=2
        skladnik=1/silnia(k)
        znak=-znak
    return(wynik)
print(zadanie())

# zadanie domowe

# napisz program ktory obliczy wartosc cos=1 korzystajac ze wzouru
# cos1=1-1/2!+1/4!+
# gracz zaczyna z 100 punktami gra polega na 3 kolejnych rzutach ksocia kazdy kolejny rzut zmienia ilosc punktow gracza wedlug ponizszego schemati
# wypadła 6 punkty pozostaja bez zmain, wypadaa 5 lub 4 punkty gracza mnozymy x2
# wypadla 3 lub 2 dzielimy 2 porzucamy czesc dziesietna
# wypadla 1 gracz traci wszystkie punty  oprocz 1
# zaimplemetnuj wynik 1 rzutu koscia funkcja rzut, napisz funkcje ktora ma przyjmowac punkty i wyniki rzutow
# a zwaracac liczbe punktow jaka otrzyma gracz na koniec gry


