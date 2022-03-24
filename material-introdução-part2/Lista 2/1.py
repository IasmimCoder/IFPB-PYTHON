#Faça um programa que solicite ao usuário dois números e mostre todos os
# resultados de possíveis de operações relacionais entre eles, ou seja, deve
# mostrar todos os resultados das operações iniciando com um número e depois
# com outro.

number1 = int(input("Escolha um número: "))
number2 = int(input("Escolha outro número: "))

print("---------------------------------------------------")
print(f"O número {number1} é maior que o número {number2}?")
print(number1 > number2)

print("---------------------------------------------------")
print(f"O número {number1} é maior ou igual ao número {number2}?")
print(number1 >= number2)

print("---------------------------------------------------")
print(f"O número {number1} é menor que o número {number2}?")
print(number1 < number2)

print("---------------------------------------------------")
print(f"O número {number1} é menor ou igual ao número {number2}?")
print(number1 <= number2)

print("---------------------------------------------------")
print(f"O número {number1} é igual ao número {number2}?")
print(number1 == number2)

print("---------------------------------------------------")
print(f"O número {number1} é diferente do número {number2}?")
print(number1 != number2)
print("---------------------------------------------------")
