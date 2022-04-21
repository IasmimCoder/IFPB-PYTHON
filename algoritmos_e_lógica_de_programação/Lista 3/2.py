#Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

number = int(input("Digite um número inteiro qualquer: "))

if (number < 0):
    print(f'O número {number} é negativo!')
else:
    print(f'O número {number} é positivo!')