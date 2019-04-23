A=input().split()
B=input().split()
length=len(A)
for x in range(2):
    if x==0:
        for y in range(length):
            val=A[y]
            A.remove(val)
            val=int(val)
            A.insert(y,val)
    else:
        length=len(B)
        for y in range(length):
            val=B[y]
            B.remove(val)
            val=int(val)
            B.insert(y,val)
        
x=list(product(A,B))
for y in x:
    print(y,end=" ")