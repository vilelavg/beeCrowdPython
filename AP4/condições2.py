valor=float(input())
cod=int(input())

if cod == 1:
    desc=valor*0.10
    pagar=valor-desc
    print("%.2f"%pagar)
    
    
elif cod == 2:
    desc=valor*0.05
    pagar=valor-desc
    print("%.2f"%pagar)
        
elif cod == 3:
    parc=valor/5
    print("%.2f"%parc)
            
elif cod == 4:
    acres=valor*0.15
    parc=(valor+acres)/10
    print("%.2f"%parc)
                
else:
    print("ERRO")