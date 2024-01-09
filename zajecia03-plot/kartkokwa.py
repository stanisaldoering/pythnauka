from math import sqrt
from math import fabs
p=[]
with open("pppunkty.txt","r") as file:
    for j in file:
        p.append(j.strip().split())

C=(4,5)
p.append(C)
print(p)

ab=sqrt((p[1][0]-p[0][0])**2+(p[1][1]-p[0][1])**2)
ac=sqrt((p[2][0]-p[0][0])**2+(p[2][1]-p[0][1])**2)
bc=sqrt(p[2][0]-p[1][0]**2+(p[2][1]-p[1][1])**2)
if ab+ac>bc:
    print("tak")
else:
    print("nie")