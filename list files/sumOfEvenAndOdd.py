element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even=0
odd=0
even_sum=0
odd_sum=0
while i<len(element):
    if element[i]%2==0:
        even+=1
        even_sum+=element[i]
    else:
        odd+=1
        odd_sum+=element[i]
    i+=1
print("sum of  even Number is",even_sum,"and sum of odd Number is",odd_sum)
