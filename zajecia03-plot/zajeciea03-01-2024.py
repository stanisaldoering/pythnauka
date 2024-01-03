from math import fabs
xa=4
ya=1
xb=1
yb=5
a=fabs(xb-xa)
b=fabs(yb-ya)
def cos(a,b):
    punkty=[]
    punkty.append(2*(a+b))
    punkty.append((a-1)*(b-1))
    return punkty
print(cos(a,b))

# jest prostokat i znajdz ilosc punktow kratowych gdy jest przekątna w prostokacie Po jednej i drugiej stronie