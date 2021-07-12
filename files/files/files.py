f=open("status.txt","r")
for i in f:
    if "delhi" in i:
        s=open("delhi.txt","a")
        s.write(i)
    elif "shimla" in i:
        d=open("simla.txt","a")
        d.write(i)
    else:
        o=open("others.txt","a")
        o.write(i)