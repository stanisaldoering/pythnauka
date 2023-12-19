# with open("punkty.txt","r")as file:
#     i=file.readline()
#     print(i)
#     print("------")
#     for j in range(3):
#         print(file.readline())
#     print("_------")
#     for _ in file:
#         print(file.readline())
lista=[]
with open("punkty.txt","r")as file:
    t=int(file.readline())
    for i in range(t):
        tmp=file.readline().split()
        lista.append((int(tmp[0]),int(tmp[1])))
    print(lista)

# wyswietl wszytskie kombiacjae polaczonych punktow
for k in range(len(lista)):
    print(lista[0]),int(lista[k+1])