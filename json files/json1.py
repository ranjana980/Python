import json
a='{"a": 1,"a": 2,"a": 3,"a": 4, "b": 1,"b": 2}'
python_object=json.loads(a)
b={}
for i in python_object:
    for j in python_object:
        if i not in b:
            b[i]=python_object[i]
print(b)