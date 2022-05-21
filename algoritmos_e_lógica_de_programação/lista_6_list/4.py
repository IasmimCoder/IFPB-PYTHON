'''
Escreva um programa para pedir ao usuário 15 números, guardar em uma lista e
imprimir a lista lida. A partir da lista, determinar o maior e o menor valor da lista e
suas respectivas posições de entrada.
'''

lista = []
maior = 0


for i in range(15):
    lista.append(int(input(f"Digite o {i+1}º número: ")))

print(f'Sua lista é {lista}')

menor = lista[0]

for elemento in lista:
    if elemento >= maior:
        maior = elemento
    if elemento <= menor:
        menor = elemento

print(f"O maior elemento é {maior} no índice {lista.index(maior)}")
print(f'O menor elemento é {menor} no índice {lista.index(menor)}')
