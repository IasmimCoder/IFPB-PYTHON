'''
Considerando uma lista de 10 números, escreva um programa que atribua a cada
elemento o valor do elemento seguinte e o último receberá o valor do primeiro.
Imprima a lista no final.
'''
import random

numeros = []

for i in range(0, 10):
    numeros.append(random.randint(1, 100))

print(numeros)

for index in range(0, len(numeros)):
    if index < len(numeros)-1:
        aux = numeros[index]
        numeros[index] = numeros[index+1]
        numeros[index+1] = aux
    else:
        aux = numeros[-1]
        numeros[-1] = numeros[0]
        numeros[0] = aux

for index, numero in enumerate(numeros):
    print(f"{index+1}º - valor = {numero} ")


