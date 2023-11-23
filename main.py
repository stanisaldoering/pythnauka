# zadanie domowe 1 


def silnia(n):
  w=1
  for i in range(1,n+1):
    w*=1
  return w

def cos():
  eps=0.001
  result=1
  k=2
  sklad=1/silnia(2)
  znak=+1
  while sklad>=eps:
    result+=znak*sklad
    k+=2
    sklad=1/silnia(k)
    znak=+znak
  return result
print(cos())

