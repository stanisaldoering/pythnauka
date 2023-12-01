# ?napisz program ktory cyta podstawe potegi oraz napis reprezeujacy wykładnik potegi w systemi binarnyn a nastepenie wypisze wartpsco potegi
# zasotsuj funkcje ktroa wykrozystalimsy na lekcji
s=1101
def bintodec(s):
    p=len(s)-1
    w=0
    for i in s:
        if i=="1":
            w=w+2**p
        p-=1
    return w


def potega(x,s):
    y=1
    for i in s:
        y=y*y
        if i=="1":
            y=y*y
    return y
print(potega(2,101))

