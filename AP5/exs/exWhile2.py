while True:
    print("iniciar(i) ou encerrar(e)")
    acao=input()

    if acao=='e':
        print("Programa encerrado")
        break

    elif acao=='i':
        print("Qual o maior/ menor numero?")
        num1=int(input("Numero 1: "))
        num2=int(input("Numero 2: "))
        maior=max(num1,num2)
        menor=min(num1,num2)
        print("Maior = ",maior)
        print("Menor = ",menor)

    else:
        print("ERRO")