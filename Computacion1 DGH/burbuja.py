lista=[32,325,12,534,124,21,2]
for k in range(1,len(lista)):
    print(lista)
    i=lista[k-1]
    j=lista[k]
    print(str(i)+' '+str(j))
    if j>i:
        lista[k-1]=j
        lista[k]=i
        for n in range(k):
            i=lista[k-1-n]
            j=lista[k-n]
            if j>i:
                lista[k-1-n]=j
                lista[k-n]=i
    else:
        pass
print(lista)
    