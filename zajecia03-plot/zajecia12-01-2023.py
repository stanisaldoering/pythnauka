# napisz program ktory wczyta tekst i wzorzec malymi literami z alafabteu lacisnkiego a nastepnie wyszuka wzorzec w tekscie stosujac algorytm naiwn
# w programie utworz funkcje znajdz

t="hhaeufbabcfhdkjsx"
w="abc"
def znajdz(t,w):
    for i in range(len(t)-len(w)+1):
        if t[i:i+len(w)]==w:
            return True
    return False
k=znajdz(t,w)
if k:
    print("jest")
else:
    print("nie ma")
l=0
for i in w:
    l=l+ord(i)
print(l)

d=[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
suma=0
for i in range(len(d)):
    suma=sum(d[i:i+3])
print(suma)

# if suma wzorca==suma(len z tekstu)