#Faça um programa que pergunte ao usuário quanto ele ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês.

preco_hora = float(input("Quanto você ganha por hora? "))
hora_mes = float(input("Quantas horas você trabalhou este mês?"))
total_salario = hora_mes*preco_hora

print(f'Então, você receberá ${total_salario} este mês!')
