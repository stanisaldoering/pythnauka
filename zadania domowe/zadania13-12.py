# zadanie 3
tekst='hhhajjthaakkacdhkh'
wzorzec="abcd"
def wzor(tekst,wzorzec):
    for i in range(0,len(tekst)-len(wzorzec)-1):
        if wzorzec[0]==tekst[i]:
            tmp=len(wzorzec)+i
            if wzorzec == tekst[i:tmp]:
                return True
    return False
print(wzor(tekst,wzorzec))

# zadanie 1
s=(1,2)
k=(3,4)

def funckja3(s,k):
    if (a*s[0]+b*s[1]+c)*(a*k[0]+b*k[1]+c)>0:
        print("leza po tej samej")
    else:
        print("nie leżą po tej samej stronie")
print(funckja3(s,k))

# zadanie 2
s=[1,2]
a=int(input("podaj wspolczynnik a: "))
b=int(input("podaj wsopolczynnik b:"))
x=range(s[0])
l=[]
for i in x:
  l.append(a*i+b)
def funckja2(l):
  if a*s[0]+b==s[1]:
    print("podany punkt leży na prostej")
  else:
    print("podany punkt nie leży na prostej")
  return l
print(funckja2(l))