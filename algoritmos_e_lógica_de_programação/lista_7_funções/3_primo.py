'''Escreva uma função em Python que receba um número inteiro como parâmetro (n)
e retorne um Boolean dizendo se ele é primo ou não. Faça um programa que use
essa função.'''

def numeroPrimo(numero):
    divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            
    if divisores > 1:
        return False
    else:
        return True

n = int(input("Digite um número: "))
trueOrFalse = numeroPrimo(n)

print(f"O número {n} é primo: {trueOrFalse}")