i=1
while i<=100:
    if i%3==0:
        print("Nav")
    elif i%7==0:
        print("Gurukul")
        if i%3==0:
            if i%7==0:
                print("Navgurukul")
        else:
            print(i)
    i=i+1