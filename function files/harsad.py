def Harsad(n):
    while n<=1000:
        x_digit=list(str(n))
        new=list(map(int,x_digit))
        if sum(new)%n==0:
            print(True)
        else:
            print(False)
        
        n=n+1
Harsad(1)
