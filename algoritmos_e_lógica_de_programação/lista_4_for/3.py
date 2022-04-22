'''Faça um programa que leia 5 números e informe a soma e a média a cada número
lido.'''

soma = 0 

for x in range(1, 6):
    number = int(input("Digite um número natural: "))
    soma += number 
    print(f"Você digitou {number}. A soma agora é {soma}.")

media = soma / x
print(f'A média é {media}')
