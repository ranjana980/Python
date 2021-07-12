# cheaking which element is not in second list
list1=[1,2,3,4,5,6,9]
list2=[2,3,0,1,6,7]
new_list=[]
i=0
while i<len(list1):
    if list1[i] not in list2:
        new_list.append(list1[i])       
    i+=1
print(new_list)