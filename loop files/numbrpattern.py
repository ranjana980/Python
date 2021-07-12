i=1
space=10
while i<10:
    print(" "*space,end="")
    j=1
    while j<=i-1:
        print(j,end="")
        j=j+1
    l=i
    while l>0:
        print(l,end="")
        l=l-1
    print()
    space=space-1
    i=i+1