'''Implemente uma função recursiva que receba uma lista de letras e retorne
uma string (concatenando as letras). Crie um programa que use essa função.'''

### FUNÇÕES ###

def concatenaLista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        
        return (lista.pop(0) + concatenaLista(lista))

### INÍCIO ###

user_list = []

n = int(input("Quantos elementos terá sua lista? "))
for i in range(n):
    elemento = str(input(f"Add o {i+1}º elemento: "))
    user_list.append(elemento)

print(f"Sua lista é {user_list}")

string = concatenaLista(user_list)
print(f"Elementos concatenados: {string}")

