def novopreco(n1):
    tax=(n1*0.1)+n1
    return ("%.2f"%tax)
def taxa(n1):
    tax=n1*0.025
    return ("%.2f"%tax)

valor=int(input())
preco=novopreco(valor)
tax=taxa(valor)
print(preco)
print(tax)