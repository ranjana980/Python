mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr="over"
list=mainStr.split()
for i in list:
    if i==substr:
        list.remove(i)
print(list)
