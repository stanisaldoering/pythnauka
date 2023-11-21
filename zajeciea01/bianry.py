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
        w*=1
    return w
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