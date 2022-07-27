lista_invertida = []

def inverte(lista):
    if len(lista) > 0:
        lista_invertida.append(lista.pop())
        inverte(lista)
    else:
       print(lista_invertida)

listaaa = [10, -1, 4]
inverte(listaaa)
