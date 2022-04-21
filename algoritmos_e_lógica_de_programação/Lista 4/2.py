'''Faça um programa que leia do usuário um número e some todos os valores de 1 até
o número passado elevados a eles mesmos.'''

numero = int(input())
soma = 0

for x in range(1, numero+1):
    soma += x**x
    print(soma)

print("SOMA = ", soma)