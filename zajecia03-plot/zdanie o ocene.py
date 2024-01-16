# import random
# from random import randint
# w=3
# k=6
# lista=[]
# for i in range(w):
#     wiersz=[]
#     for  j in range(k):
#         l=random.randint(1,1100000)
#         wiersz.append(l)
#     lista.append(wiersz)
# for i in lista:
#     print(wiersz)
#
# for i in range(w):
#     suma_w=sum(lista[i])
#     for j in range(k):
#         suma_kolumny=sum([lista[k][j]for k in range(w)])
#         for k in range(w):
#             if suma_w==suma_kolumny:
#                 print("wiersz",i+1)
#                 print("kolumna",j+1)
#             else:
#                 print("BRAK")
# # # def los(n):
#     lista=[]
#     for i in range(n):
#         lista.append(randint(0,100))
#     return lista
# lista=los(7)
# print(lista)
import random

# Funkcja do tworzenia dwuwymiarowej listy losowych liczb całkowitych
def stworz_liste(wiersze, kolumny):
    lista = [[random.randint(1, 10) for _ in range(kolumny)] for _ in range(wiersze)]
    return lista

# Funkcja do sprawdzania sum wierszy i kolumn
def sprawdz_sumy(lista):
    for i in range(len(lista)):
        suma_wiersza = sum(lista[i])
        for j in range(len(lista[0])):
            suma_kolumny = sum(lista[k][j] for k in range(len(lista)))
            if suma_wiersza == suma_kolumny:
                return f"Wiersz: {i+1}, Kolumna: {j+1}"
    return "BRAK"

# Tworzenie i wyświetlanie listy dwuwymiarowej
wiersze = 4
kolumny = 4
lista_dwuwymiarowa = stworz_liste(wiersze, kolumny)
print("Lista dwuwymiarowa:")
for wiersz in lista_dwuwymiarowa:
    print(wiersz)

# Sprawdzanie sum wierszy i kolumn
wynik = sprawdz_sumy(lista_dwuwymiarowa)
print("Wynik sprawdzenia:")
print(wynik)