limite = 50
peso=float(input())

if peso > limite:
    exc=peso-50
    multa=exc*4

    print("%.2f"%exc)
    print("%.2f"%multa)

elif peso > 0 and peso <=50:
    bonus=peso*1
    print("%.2f"%bonus)

else:
    print("ERRO")