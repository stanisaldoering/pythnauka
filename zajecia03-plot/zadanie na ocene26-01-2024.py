
# w="hfhakckajrkfnabjafbfj"
# m=len(w)
# klucz=[]
# for i in range(k):
#     klucz.append(a)
#     a=a+1
#
# k=len(klucz)
def szyfruj(n):
    s = ""
    if n+k-1<m:
        for i in range(0,k):
            s=s+w[n+klucz[i]-1]
        szyfruj(n+k)
    else:
        while n<=m:
            if n<m:
                s=s+w[n]-w[n-1]
                n=n+2
            else:
                s=s+w[n]
                n=n+1
w="kolorado"
m=len(w)
klucz=[1,2,0]
k=3
print(szyfruj(1))