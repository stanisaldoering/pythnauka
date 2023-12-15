lista=["Adam Nowak","Jan kowalski","Maria Zawadzka","Anna Zaradzka","Tomasz Nowak"]
Inicjaly=[]
for i in range(len(lista)):
  x=lista[i]
  Inicjaly.append(x[0]+x[x.find(" ")+1])
print(Inicjaly)
