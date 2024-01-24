from random import randint
def los(n):
    A=[]
    for i in range(n):
        A.append(randint(0,100))
    return A
A=los(5)
A.sort()

# def spr(A):
#     n=len(A)
#     for i in range(n-1):
#         if A[i]==A[i+1]:
#             return False
#     return True
# print(spr(A))

def cos(A):
    n=len(A)
    tmp=[]
    for i in range(n-1):
        if A[i]==A[i+1]:
            tmp.append(A[i])
        if len(tmp)==(len(A)//2):
            return True
    return False
print(cos(A))