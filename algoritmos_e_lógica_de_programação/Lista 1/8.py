#Escreva um programa que peça ao usuário dois números naturais que representam a base e a altura de um triângulo, respectivamente, e calcule a sua área.

base = float(input("Qual o valor da base do triângulo? "))
altura = float(input("E qual o valor da altura do triângulo? "))

area = float(base*altura)/2

print("A área desse triângulo é", area)
