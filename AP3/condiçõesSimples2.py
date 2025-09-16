area=float(input())
litrosNec=area/3

latas=int(litrosNec//18)
if litrosNec % 18 != 0:
    latas=latas+1

total=latas*120

print(latas)
print("%.2f"%total)