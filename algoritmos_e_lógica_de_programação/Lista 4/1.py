'''Faça um programa que leia 5 números inteiros do usuário. Daí, imprima quantos
números positivos, negativos, pares e ímpares foram passados. Lembre-se que o 0
nem é positivo nem negativo. Imprima também a média de todos os valores, ao final.'''

qtd_positivos = 0
qtd_negavitos = 0
qtd_pares = 0
qtd_impares = 0
valor_total = 0 

for x in range(1, 6):
    numero = int(input(f"digite o {x}º valor: "))
    valor_total += numero
    if numero > 0: 
        qtd_positivos += 1
    elif numero < 0:
        qtd_negavitos += 1
    
    if numero % 2 == 0:
        qtd_pares += 1
    elif numero %2 != 0:
        qtd_impares += 1

media = valor_total / x

print(f"Você digitou: {qtd_positivos} números positivos, {qtd_negavitos} negativos, {qtd_pares} pares e {qtd_impares} ímpares.")
print(f"A média é {media}")
