while True:
    print('\nSoma.....+'+
          '\nSubtracao.....-'+
          '\nMultiplicacao.....*'+
          '\nSair.....0')
    
    op=input()
    if op=='0':
        break
    if op=='+':
        print("Soma")
        num1=float(input("Numero 1: "))
        num2=float(input("Numero 2: "))
        res=num1+num2
        print()
        print("Resultado = ",num1+num2)

    elif op=='-':
        print("Subtracao")
        num1=float(input("Numero 1: "))
        num2=float(input("Numero 2: "))
        res=num1-num2
        print()
        print("Resultado = ",num1-num2)

    elif op=='*':
        print("Multiplicação")
        num1=float(input("Numero 1: "))
        num2=float(input("Numero 2: "))
        print()
        print("Resultado = ",num1*num2)

    else:
        print("ERRO") 