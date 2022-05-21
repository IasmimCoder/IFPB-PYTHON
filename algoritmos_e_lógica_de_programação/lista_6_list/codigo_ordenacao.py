lista = [ 2 , 5 , 1, 213, 3]

for i in range(len(lista)):
    for l in range(i+1, len(lista)):
        if lista[i] > lista[l]:
            aux = lista[i]
            lista[i] = lista[l]
            lista[l] = aux
