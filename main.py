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

x=int(input("podaj wartosc x"))
s=int(input("podaj stopien wielomianu"))
def stopien(s):
  lista=[]
  for i in range(0,s+1):
    lista.append(int(input("podaj wspolczynnik przy x^"+str(i))))
  return lista
# print(stopien(s))

def wielomian(x,lista):
  wynik=0
  for i in range(0,len(lista)):
    wynik+=lista[i]*(x**i)
  return wynik
print(wielomian(x,stopien(s)))