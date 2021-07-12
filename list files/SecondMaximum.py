numbers=[50,40,23,70,56,12,5,10,7]
i=0
s=numbers[1]
while i<len(numbers):
    m=numbers[i]
    if m>s:
        s=m
    i+=1
numbers.remove(s)
k=0
j=numbers[1]
while k<len(numbers):
    n=numbers[k]
    if n>j:
        j=n
    k+=1
print(j)
