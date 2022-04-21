#Faça um programa que solicite ao usuário dois números e mostre todos os
# resultados de possíveis de operações relacionais entre eles, ou seja, deve
# mostrar todos os resultados das operações iniciando com um número e depois
# com outro.

number1 = int(input("Escolha um número: "))
number2 = int(input("Escolha outro número: "))

print("---------------------------------------------------")
print(f"O valor da avaliação da expressão {number1} > {number2} é ")
print(number1 > number2)

print("---------------------------------------------------")
print(f"O valor da avaliação da expressão {number1} >= {number2} é ")
print(number1 >= number2)

print("---------------------------------------------------")
print(f"O valor da avaliação da expressão {number1} < {number2} é ")
print(number1 < number2)

print("---------------------------------------------------")
print(f"O valor da avaliação da expressão {number1} <= {number2} é ")
print(number1 <= number2)

print("---------------------------------------------------")
print(f"O valor da avaliação da expressão {number1} == {number2} é ")
print(number1 == number2)

print("---------------------------------------------------")
print(f"O valor da avaliação da expressão {number1} != {number2} é ")
print(number1 != number2)
print("---------------------------------------------------")
