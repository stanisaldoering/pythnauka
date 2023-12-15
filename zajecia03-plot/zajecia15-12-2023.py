import matplotlib.pyplot as plt
x=[i for i in range(-5,6)]
y=[]
a=int(input("podaj wspolczynik a"))
b=int(input("podaj wspolczynnik b"))
# y=2x-3
for i in x:
    y.append(a*i-b)

plt.plot(x,y)
plt.plot(x,y,"ro")
# daje kropki
plt.plot(color="green",linestyle="--",linewidth=1)
plt.show()