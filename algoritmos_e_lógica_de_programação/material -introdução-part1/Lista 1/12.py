#Escreva um programa que leia uma temperatura em graus Celsius e a apresente
# convertida em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160) / 5,
# sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

temp_celsius = float(input("Qual a temperatura em graus Celsius? "))
fahrenheit = (9*temp_celsius+160)/5

print("Então a temperatura em Fahrenheit é",fahrenheit,"!")
