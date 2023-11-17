def binFloat(n,ilebit=0):
    wynik=0
    for i in range(2,ilebit+2):
        if n[i]=="1" or n[i]=='0':
            if n[i]=='1':
                wynik+=2**(-i+1)
        else:
            return 'error'
    return(wynik)


print("y1",x-y1)
print("y2",x-y2)
print("y3",x-y3)
# wratosc dokladna x=0,1 w systemie dziesietny jest rowna 0,1 oblicz jaki bedzie blad przy zapisie liczby 0,1 z wykorzytsaniem 8 bit,12, 16

# napisz program  ktroy obliczby  wartosc sinusa 1 korzystajac ze wzoru sin
# obliczenia wykonaj z dokladnoscia do 4 liczb