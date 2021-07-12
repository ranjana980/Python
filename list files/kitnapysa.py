kitna_pysa_hai=[3000,600000,3249909009,30000,560000,690909090,31010101,532010,510,4100]
crorepati=0
lakhpati=0
dilwale=0
i=0
while i<len(kitna_pysa_hai):
    if kitna_pysa_hai[i]>=10000000:
        crorepati+=1
    elif kitna_pysa_hai[i]>=100000:
        lakhpati+=1
    else:
        dilwale+=1
    i+=1
print(crorepati,"carorepati",lakhpati,"lakhpati",dilwale,"dilwale")
