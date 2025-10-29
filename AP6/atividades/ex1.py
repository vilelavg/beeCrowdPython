par=0
impar=0
op=int(input())
for i in range(1,op+1):
    n=int(input())
    if n%2==0:
        par+=1
    else:
        impar+=1
print(par)
print(impar)