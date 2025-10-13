invest=int(input())
aplic=float(input())
prazo=int(input())

if invest == 1:
    percent=0.5/100
    valorf=aplic * (1 + percent)**prazo
    print("%.2f"%valorf)

elif invest == 2:
    p=0.8/100
    valorf=aplic * (1+p)**prazo
    print("%.2f"%valorf)

elif invest == 3:
    p=1/100
    valorf=aplic * (1+p)**prazo
    print("%.2f"%valorf)
else:
    print("ERRO")