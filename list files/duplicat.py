from typing import List


list=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
dict1=[]
duplicate=[]
i=0
while i<len(list):
    if list[i] not in dict1:
        dict1.append(list[i])
    else:
        duplicate.append(list[i])
    i+=1
print(duplicate)
