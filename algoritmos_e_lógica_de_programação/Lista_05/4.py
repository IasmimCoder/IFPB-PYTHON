'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares. Mostre uma mensagem caso o
valor não seja válido e continue pedindo até que o usuário informe, ao total, os 10
valores válidos.
'''

number = 0
pares = 0
impares = 0
vezes = 1

while vezes < 11: 

    number = int(input(f"Digite o {vezes}º número inteiro: "))


    if number % 2 == 0:
        pares += 1 
    elif number % 2 != 0:
        impares += 1

    vezes += 1

print(f'QTD DE NÚMEROS PARES: {pares}')
print(f'QTD DE NÚMEROS ÍMPARES: {impares}')

