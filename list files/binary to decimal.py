a=[1,0,0,1,1,0,1,1]
s=0
sum=0
n=len(a)-1
i=0
while i<len(a):
    m=a[n]
    s=(2**i)*m
    i+=1
    n-=1
    sum+=1
print(sum)
