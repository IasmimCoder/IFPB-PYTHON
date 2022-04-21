#Faça um programa que peça dois números e imprima o maior deles.

number1 = int(input("Digite um número inteiro: "))
number2 = int(input("Digite outro número inteiro: "))

if (number1 > number2):
    print(f'O número {number1} é maior que o número {number2}!')
elif (number2 > number1):
    print(f'O número {number2} é maior que o número {number1}!')
else:
    print("O números são iguais!")
