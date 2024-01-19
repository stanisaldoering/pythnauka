# i<=i+k
lista=[]
with open("pilotka.txt","r") as file:
    for j in file:
        lista.append(j.strip())
print(lista)
# def fun(lista,k):
#     for i in range(len(lista)-k):
#         if lista[i]<=lista[i+k]:
#             print(k)
#             return True
#         return False
# print(fun())
# for o in range(2,100):
#     if fun(lista,k):
#         print(i)



# def cos(lista,k):
#     for i in range(len(lista)-k):
#         if lista[i]>lista[i+k]:
#             return False
#     return True
# print(cos())
# for i in range(2,100):
#     if cos():
#         print(i)

#w pliku liczby txt znajudje sie 1000 roznych liczb o dlugosci od 2 do 9 cyfr napisz funkcje lub program ktory da odpowiedz na ponizse pytania
# czynnikiem danej liczby naturalnej zlozonej jest dowolona liczba pierwsza ktora dzieli calkowicie podaj w pliku jest iczb txt liczb w ktoych rozkladzie na czynnik pierwsze
# wystepuje 3 rozne czynniki, czynniki mozga sie powtarzac z ktorych kazdy jest nie parzyse


# 1 pobrac se liczby do listy
# 2 sprawdzic ktore liczby sa liczbami pierwszymi
# 3 wypisac wszystkie czynniki do maybe kolejnej listy
# 4 poszukac powtarzajace sie czynniki i dodac do lity
# 5 jesli sa czynniki ktore powtarzaja sie 3 razy to ma wyswietlic liste