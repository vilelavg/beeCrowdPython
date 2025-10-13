precog=0

while True:
    produto=input()
    if produto=='fim':
        break
    units=int(input())
    preco=float(input())    
    precof=units*preco
    precog+=precof
    print("%.2f"%precof)    

print("%.2f"%precog)