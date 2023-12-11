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