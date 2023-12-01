# # napisz program ktory obliczy wartosc wielomianu algorytem naiwnym  wykorzystujacy funkcje pobierania argumentu o podanym stopniu wielomianu
# x=int(input("podaj x"))
# s = int(input("podaj stopien wielomianu"))
# def stopien(s):
#     stopnie=[]
#     for i in range(0,s+1):
#         stopnie.append(i)
#     return stopnie
# print(stopien(s))

# x=int(input("podaj wartosc x"))
# s=int(input("podaj stopien wielomianu"))
# def stopien(s):
#   lista=[]
#   for i in range(0,s+1):
#     lista.append(int(input("podaj wspolczynnik przy x^"+str(i))))
#   return lista
# # print(stopien(s))
#
# def wielomian(x,lista):
#   wynik=0
#   for i in range(0,len(lista)):
#     wynik+=lista[i]*(x**i)
#   return wynik
# print(wielomian(x,stopien(s)))

x=3
s=4
listaarg=[3,2,1,-1,-2]
def wielo(x,s,lista):
    listaarg.reverse()
    w=1
    wielomian=listaarg[0]
    print(wielomian)
    for i in range(1,s+1):
        w*=x
        wielomian+=w*listaarg[i]
        print(wielomian)
    return wielomian
res=wielo(x,s,listaarg)
print(res)
