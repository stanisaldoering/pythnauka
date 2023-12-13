import math
punkty=[(1,2),(3,4)]
def dlugoscodc(p1,p2):
  return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**math.sqrt
print(dlugoscodc(punkty[0],punkty[1]))