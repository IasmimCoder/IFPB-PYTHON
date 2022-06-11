'''5) Faça uma função recursiva que calcule a soma dos dígitos de um número.
Por exemplo, se a entrada for 123, a saída deverá ser 1+2+3 = 6. A entrada
é uma string. Crie um programa que use essa função. (string só com
números positivos).'''


### FUNÇÕES ###


def somaNum(numeros):
    if numeros == "":
        print(" = ", end="")
        return 0    
    print(numeros[0], end="")
    if len(numeros) != 1:
        print(" + ", end="")
    
    return int(numeros[0]) + somaNum(numeros[1:])

### INÍCIO ###

numbers = input("Digite um número inteiro positivo: ")

print(somaNum(numbers))
