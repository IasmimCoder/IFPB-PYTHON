'''
Faça um programa que peça ao usuário um número natural N, depois peça N
números entre 0 e 1000 ao usuário e imprima a soma dos valores. Faça validação
de todas as entradas.
'''

n = int(input("Digite um número N qualquer natural: "))

soma = 0

while n < 0:
    n = int(input("Digite somente um número N qualquer natural: "))

for x in range(1, n+1):
    number = int(input(f"Digite o {x}º número de 0 a 1000: "))

    while number < 0 or number > 1000: 
        number = int(input(f"Erro! Digite o {x}º número, apenas na faixa de 0 a 1000: "))

    soma += number

print(f'A soma dos números é de {soma}.')
