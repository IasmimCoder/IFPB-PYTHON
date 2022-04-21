#Faça um programa que peça dois números naturais ao usuário e imprima a exponenciação desses números.

num1 = int(input("Digite um número natural de 1 a 100: "))
num2 = int(input("Digite um segundo número natural de 1 a 100: "))

expon = num1 ** num2

print("A exponenciação entre os numéros",num1,"e",num2,"é",expon)
