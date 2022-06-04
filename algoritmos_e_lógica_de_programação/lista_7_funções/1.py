'''Escreva uma função em Python que receba dois números inteiros como parâmetro
e retorne o valor do primeiro elevado ao segundo. Faça um programa que use essa
função.'''

def exponenciação(a, b):
    x = a ** b

    return x

valor_a = int(input("Escolha a base da sua exponenciação: "))
valor_b = int(input("Escolha o expoente: "))

total = exponenciação(valor_a, valor_b)
print(f"Sua exponenciação é {total}")
