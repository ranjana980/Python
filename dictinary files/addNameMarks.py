dic={}
i=0
while i<=10:
    name=input("enter your name")
    marks=input("enter your marks")
    j=0
    while j<len(name):
        dic[name]=marks
        j=j+1
    i=i+1
print(dic)