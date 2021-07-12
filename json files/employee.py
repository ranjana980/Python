a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
f=["name","Diestaions","age","salary"]
employee1={}
employee2={}
employee3={}
employee4={}
dic1={}
i=0
while i<len(a):
    j=0
    while j<len(f):
        employee1[f[j]]=a[j]
        j=j+1
    i=i+1
dic1["employee1"]=employee1
k=0
while k<len(b):
    l=0
    while l<len(f):
        employee2[f[l]]=b[l]
        l=l+1
    k=k+1
dic1["employee2"]=employee2
m=0
while m<len(c):
    n=0
    while n<len(f):
        employee3[f[n]]=c[n]
        n=n+1
    m=m+1
dic1["employee3"]=employee3
p=0
while p<len(d):
    r=0
    while r<len(f):
        employee4[f[r]]=d[r]
        r=r+1
    p=p+1
dic1["employee4"]=employee4
print(dic1)


    