from math import sqrt
from math import fabs

# def pitagoras(punkty):
#     x1,y1 = punkty[0]
#     x2,y2 = punkty[1]
#     a = fabs(x2-x1)
#     b = fabs(y2-y1)
#     c = sqrt(a**2+b**2)
#     return a,b,c
#
# def polepopunkt(punkty):
#     a,b,c = pitagoras(punkty)
#     p = (a+b+c)/2
#     Pole = sqrt(p*(p-a)*(p-b)*(p-c))
#     return Pole
#
# punkty = [[1,2],[5,4]]
#
# print("pole =",polepopunkt(punkty))

from math import sqrt
from math import fabs
# def boki(punkty):
#     x1,y1 = punkty[0]
#     x2,y2 = punkty[1]
#     a = fabs(x2-x1)
#     b = fabs(y2-y1)
#     return a,b
#
# # def punkt_krat(punkty):
# #     a,b = boki(punkty)
# #     pnkty_krat_wew = (a-1)*(b-1)
# #     punkt_krat_zewn = 2*(a+b)
# #     punkt_krat_wsz = punkt_krat_zewn + pnkty_krat_wew
# #     return int(punkt_krat_wsz)
# :
#
# punkty = [[1,2],[5,4]]
#
# print("punkty =",punkt_krat(punkty))
A=[0,0]
B=[4,4]
lista=[]
def det(x1, y1, x2, y2, x3, y3) :
    return (y3-y1)*(x2-x1)-(y2-y1)*(x3-x1)
def kratowe( pktA, pktB):
    licznik1 = 0
    licznik2 = 0
    for i in range(A[0],B[0]+1):
        for j in range(A[1],B[1]+1):
            w = det(pktA[0], pktA[1], pktB[0], pktB[1], i, j)
            if w < 0:
                licznik1 += 1
            elif w > 0:
                licznik2 += 1
        return [licznik1, licznik2]
wynik = kratowe([1,1],[4,10])
print("Po jednej stronie prostej znajduje sie " , wynik[0], " punktow")
print("Po drugiej ", wynik[1], " punktow.")
pkt=[]
C=[]
L=[]
with open("punkt.txt","r")as file:
    for i in file:
        pkt.append(i.strip().split())
print(pkt)
for i in C:
    t=[]
    for j in i:
        t.append(int(j))
    p1=[t[0],t[1]]
    p2=[t[2],t[3]]
    pkt.append([p1,p2])
print(pkt)

print(C)
# jest prostokat i znajdz ilosc punktow kratowych gdy jest przekątna w prostokacie Po jednej i drugiej stronie
#