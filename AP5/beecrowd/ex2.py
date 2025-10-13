amountini=1000

while True:
    print('\nSaldo.....saldo'+
          '\nDeposito.....deposito'+
          '\nSaque.....saque'+
          '\nSair.....sair')
    op=input()
    if op=='sair':
        print("Programa encerrado")
        break
    if op=='saldo':
        print("Saldo atual: R$ %.2f"%amountini)
    if op=='deposito':
        valor=float(input())
        if valor<=0:
            print("Valor invalido. Tente novamente")
            while valor<=0:
                valor=float(input())
                if valor>0:
                    break
        amountini+=valor
        print("Saldo atualizado")
    if op=='saque':
        valor=float(input())
        if valor>amountini:
            print("Saldo insuficiente. Tente novamente")
            while valor>amountini:
                valor=float(input())
                if valor<=amountini:
                    break
        amountini-=valor
        print("Saque realizado!")