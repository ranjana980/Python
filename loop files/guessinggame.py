i=5
n=1
a=10
while n<=a:
    s=int(input("enter the number"))
    if s==i:
        print("congretulations,you won!")
        break
    elif s!=i and s<a:
        print("you have",a-s,"chance")
    else:
        print("you have no chance")
    a=a-s