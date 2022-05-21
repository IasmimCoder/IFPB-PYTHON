'''(20) Faça um programa que mostre os N termos da série apresentada abaixo. Peça
N, um número natural, ao usuário. Ao final, imprima a soma da série. Faça todas as
validações necessárias.

S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.'''

termo_a = 1 
termo_b = 1 
soma = 1

n = int(input("Digite um número natural: "))

while n < 1: 
    n = int(input("Digite um número natural: "))

for i in range (1, n):
    termo_a += 1
    termo_b += 2
    soma += termo_a/termo_b

print(f'Soma = {soma}')
