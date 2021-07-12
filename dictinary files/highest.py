
dic={"a":23,"b":12,"c":45,"d":34}
a=sorted(dic.values())
lenght=len(a)
i=lenght-1
list=[]
while i>=0:
    m=a[i]
    list.append(m)
    if i==lenght-3:
        break
    i=i-1
print(list)