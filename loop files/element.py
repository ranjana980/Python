counter=0
string="navgurukul"
while(counter<len(string)):
    counter+=1
    if string[counter]=="a":
        continue
    if string[counter]=="u":
        continue
    print(string[counter])
print("the end",string[counter])