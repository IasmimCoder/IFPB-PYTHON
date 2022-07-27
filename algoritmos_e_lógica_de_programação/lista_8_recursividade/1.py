'''1) Implemente a função recursiva que recebe uma posição e retorna o valor
fibonacci daquela posição (ex.: Fib(1)=1, Fib(2)=1, Fib(3)=2). Crie um
programa que use essa função.'''

### FUNÇÕES ###
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

### INÍCIO ###

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
n = int(input())
print(f"Fib({n}) = {fibonacci(n)}")
