import matplotlib.pyplot as plt
x=[i for i in range(-5,6)]
y=[j for j in range(-10,20)]
k=[]
k.append(x,y)
fk=[]
a=int(input("podaj wspolczynik a"))
b=int(input("podaj wspolczynnik b"))
c=int(input("podaj wspolczynnik c"))
# y=2x-3
for i in y:
    fk.append(a**i-(b*j)+c)

plt.plot(x,y)
plt.plot(x,y,"ro")
# daje kropki
plt.plot(color="green",linestyle="--",linewidth=1)
plt.show()