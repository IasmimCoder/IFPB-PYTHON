'''Faça um programa que peça ao usuário 20 números inteiros e armazene-os numa
lista. Depois, armazene os números pares na lista “pares” e os números ímpares na
lista “impares”. Imprima as três listas ao final.'''

numeros = [1, 2, 3]
pares = []
impares = []

for i in range(20):
    numeros.append(int(input(f"Digite o {i+1}º número inteiro: ")))

    if numeros[-1] % 2 == 0:
       pares.append(numeros[-1]) 
    else:
        impares.append(numeros[-1])

print(f'Números = {numeros}')
print(f'São pares = {pares}')
print(f'São ímpares = {impares}')
