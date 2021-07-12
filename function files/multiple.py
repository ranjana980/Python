def multiply(list):
    i=0
    multiple=1
    while i<len(list):
        multiple=multiple*list[i]
        i=i+1
    print(multiple)
multiply([8,2,3,-1,7])