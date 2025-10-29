fat=1
print()
num=int(input())
while num<0:
    num=int(input())
for a in range (1,num+1):
    fat*=a
print(fat)