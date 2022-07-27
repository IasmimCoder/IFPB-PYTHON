
def maior_da_lista(lista):
    if len(lista) == 1:
        return lista[0]

    maior = maior_da_lista(lista[1:])

    if lista[0] > maior:
        maior = lista[0]

    return maior 
      
lista = [1, 4, 9, 3, 2]
print(maior_da_lista(lista))
