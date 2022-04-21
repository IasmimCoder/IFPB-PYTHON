#Faça um programa que leia 3 valores e escreva a soma dos 2 maiores.

number1 = int(input("Digite um número inteiro: "))
number2 = int(input("Digite outro número inteiro: "))
number3 = int(input("Digite mais um número inteiro: "))
soma = 0

if ((number1 > number2 > number3) or (number2 > number1 > number3)):
     soma = number1 + number2
elif ((number1 > number3 > number2) or (number3 > number1 > number2)):
    soma = number1 + number3
elif ((number2 > number3 > number1) or (number3 > number2 > number1)):
    soma = number2 + number3


print(f'O resultado da soma entre os dois maiores números é {soma}')
