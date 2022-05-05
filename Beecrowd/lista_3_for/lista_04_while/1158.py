'''
Soma de Ímpares Consecutivos III

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste de dois inteiros X e Y. 
Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma dos consecutivos números ímpares a partir do valor X.
'''

n = int(input())
testes = 0
soma = 0 

while testes != n:
    testes += 1
    
    x,y = input().split(" ")
    x = int(x)
    y = int(y)

    if x % 2 == 0:
        soma = x+1 
        number = soma
        for i in range(y-1):
            number += 2
            soma += number
        print(soma)
            
    if x % 2 != 0: 
        soma = x
        number = soma
        for i in range(y-1):
            number += 2
            soma += number
        print(soma)
