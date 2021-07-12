element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even=0
odd=0
while i<len(element):
    if element[i]%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print("total even Number is",even,"and total odd Number is",odd)
