#Escreva um programa que leia um número e imprima se este número é ímpar ou par.

number = int(input("Digite um número inteiro qualquer: "))

if (number %2 == 0):
    print(f'O número {number} é par!')
else:
     print(f'O número {number} é impar!')