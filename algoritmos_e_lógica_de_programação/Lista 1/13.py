#Escreva um programa que calcule o valor total da conta do posto de gasolina, 
# dada a quantidade de litros abastecidos e o valor por litro.

preco = float(input("Qual o valor atual do litro da gasolina? R$"))
litros = float(input("Quantos litros você deseja abastecer? "))

total = preco*litros

print("Okay! O preço total é de R$",total)
