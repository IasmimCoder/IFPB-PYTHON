'''Escreva uma função recursiva que recebe uma lista de números e retorna a lista invertida.
Exemplo: para a lista [10, -1, 4] a função deve retornar [4, -1, 10]'''

def inverter(lista):
    if not lista: # lista vazia, retorna ela mesma
        return lista
    return lista[-1:] + inverter(lista[:-1])

lista = inverter([1, 2, 3, 4, 5])
print(lista) # [5, 4, 3, 2, 1]
