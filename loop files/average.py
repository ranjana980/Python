sum=0
s=0
while s<11:
    i=int(input("enter the number"))
    sum=sum+i 
    average=sum//11
    s=s+1
print(average)
if average%5==0:
    print("it is divisble by 5")
else:
    print("it is not divisble by 5")