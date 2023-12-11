# zadanie domowe 1 


# def silnia(n):
#   w=1
#   for i in range(1,n+1):
#     w*=1
#   return w
# print(silnia(7))
# def cos():
#   eps=0.001
#   result=1.0
#   k=2
#   sklad=1/silnia(k)
#   znak=+1
#   while sklad>=eps:
#     result+=znak*sklad
#     k+=2
#     sklad=1/silnia(k)
#     znak=+znak
#   return result
# print(cos())

# def silnia(n):
#     w=1
#     for i in range(1,n+1):
#         w*=1
#     return w
# print(silnia(7))
# def zadanie():
#     eps=0.00001
#     wynik=1.0
#     k=3
#     skladnik=1/silnia(3)
#     znak=-1
#     while skladnik>=eps:
#         wynik+=znak*skladnik
#         k+=2
#         skladnik=1/silnia(k)
#         znak=-znak
#     return(wynik)
# print(zadanie())

# x=int(input("podaj wartosc x"))
# s=int(input("podaj stopien wielomianu"))
# def stopien(s):
#   lista=[]
#   for i in range(0,s+1):
#     lista.append(int(input("podaj wspolczynnik przy x^"+str(i))))
#   return lista
# # print(stopien(s))

# def wielomian(x,lista):
#   wynik=0
#   for i in range(0,len(lista)):
#     wynik+=lista[i]*(x**i)
#   return wynik
# print(wielomian(x,stopien(s)))


# zadanie 1
# 1. Napisz program, ktory wczyta dwa wielomiany, a nastepnie wyznaczy wielomian
# bedacy ich suma i go wypisze.

# x=int(input("podaj wartosc x"))
# s=int(input("podaj stopien wielomianu"))
# lista=[]
# def stopien(s):
#   for i in range(0,s+1):
#     lista.append(int(input("podaj wspolczynnik przy x^"+str(i))))
#   return lista
# print(stopien(s))

# y=int(input("podaj wartosc drugiego wielomianu"))
# k=int(input("podaj stopein drugiego wielomianu"))
# lista2=[]
# def drugiwielo(k):
#   for i in range(0,k+1):
#     lista2.append(int(input("podaj wspolczynnik przy x^"+str(i))))
#   return lista2
# print(drugiwielo(k))

# wynik=[]
# for i in range(0,len(lista)):
#   wynik.append(lista[i]+lista2[i])
# print(wynik)
# for i in range(0,len(wynik)):
#   print(wynik[i],"x^"+str(i))


# zadanie 2 
# x=int(input("podaj wartosc x"))
# s=int(input("podaj stopien wielomianu"))
# lista=[]
# def stopien(s):
#   for i in range(0,s+1):
#     lista.append(int(input("podaj wspolczynnik przy x^"+str(i))))
#   return lista
# print(stopien(s))

# y=int(input("podaj wartosc drugiego wielomianu"))
# k=int(input("podaj stopein drugiego wielomianu"))
# lista2=[]
# def drugiwielo(k):
#   for i in range(0,k+1):
#     lista2.append(int(input("podaj wspolczynnik przy x^"+str(i))))
#   return lista2
# print(drugiwielo(k))

# wynik=[]
# for i in range(0,len(lista)):
#   wynik.append(lista[i]*lista2[i])
# print(wynik)
# for i in range(0,len(wynik)):
#   print(wynik[i],"x^"+str(i))
# zada

text="jdsjhddhda"
x="a"
list=[]
def zadanie(text,x):
  for i in range(0,len(text)):
    if text[i]==x:
      list.append(i)
  return list
print(zadanie(text,x))


lista=["Adam Nowak","Jan kowalski","Maria Zawadzka","Anna Zaradzka","Tomasz Nowak"]
Inicjaly=[]
for i in range(len(lista)):
  x=lista[i]
  Inicjaly.append(x[0]+x[x.find(" ")+1])
print(Inicjaly)

tekst='abcccaaaaaaeeeeddddd'
wzorzec='abcd'
def wzor(tekst,wzorzec):
  for i in range(len(tekst),len(wzorzec)+1):
    if i==wzorzec:
      return True 
  return True
print(wzor(tekst,wzorzec))
      
    