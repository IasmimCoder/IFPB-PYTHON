'''Escreva uma função em Python que receba um número inteiro como parâmetro (n)
e retorne uma lista com os n primeiros números da sequência de Fibonacci. Faça
um programa que use essa função.'''

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
fibonacci_list = []

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n -1) + fibonacci(n - 2)

n = int(input())

for i in range(n):
    elemento = fibonacci(i)
    fibonacci_list.append(elemento)

print(fibonacci_list)
