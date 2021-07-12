a="MISSISSIPPI" 
b=[]
for i in a:
    if i in a:
        if i not in b:
            b.append(i)
j=0
dic={}
while j<len(b):
    n=0
    count=0
    while n<len(a):
        if a[n]==b[j]:
            count=count+1
        n=n+1
    dic[b[j]]=count
    j=j+1
print(dic)
