# napisz funkcje sprawdzającą czy dwa punkty leżą dwa punkty leza po tej samej stronie prostej
# podając wartosci A,B,C równania ogolnego prostej
a=int(input("podaj punkt a"))
b=int(input("podaj punkt b"))
c=int(input("podaj punkt c"))
s=(1,3)
k=(2,4)
# l=a+b+c
# def funkcja1(s):
#     if a*s[0]+b*s[1]+c<0:
#         print("pod prosta")
#     else:
#         print("nad prostą")
# print(funkcja1(s))
# def funkcja2(k):
#     if a*k[0]+b[1]+c<0:
#         print("pod prosta")
#     else:
#         print("nad prostą")
# print(funkcja2(k))
#
# if funkcja2(k) and funkcja1(s)<0:
#     print("punkty leza po tej samej stronie")
# else:
#     print("punkty leza po innych stronach")
def funckja3(s,k):
    if (a*s[0]+b*s[1]+c)*(a*k[0]+b*k[1]+c)>0:
        print("leza po tej samej")
    else:
        print("nie")
print(funckja3(s,k))
# cos
