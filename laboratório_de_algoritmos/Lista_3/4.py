'''
Salários
A PassaAlcool70 tem três tipos de funcionários: gerente (GER), vendedor (VEN) e
estoquista (EST). Hoje, a loja conta com 1 gerente, 3 vendedores e 2 estoquistas. Faça
um programa para mostrar o salário de todos os funcionários, sabendo que o salário
bruto do gerente é R$2300,00, do vendedor é R$2000,00 e do estoquista é R$1650,00.
O imposto de renda é retido na fonte e é de 12%, porém valores até R$1700,00 são
isentos. Perceba que a alíquota só incide sobre o valor que extrapola a faixa de isenção.
'''
funcionario = ["Gerente", "Vendedor 1", "Vendedor 2", "Vendedor 3", "Estoquista 1", "Estoquista 2"]

print(funcionario[0])
salario = 2300 - (2300*0.12)
print(f'SALÁRIO LÍQUIDO= ${salario}')

print("-----------------------------")

print(funcionario[1])
salario = 2000 - (2000*0.12)
print(f'SALÁRIO LÍQUIDO= ${salario}')

print("-----------------------------")

print(funcionario[2])
salario = 2000 - (2000*0.12)
print(f'SALÁRIO LÍQUIDO= ${salario}')

print("-----------------------------")

print(funcionario[3])
salario = 2000 - (2000*0.12)
print(f'SALÁRIO LÍQUIDO= ${salario}')
 
print("-----------------------------")

print(funcionario[4])
salario = 1650
print(f'SALÁRIO LÍQUIDO= ${salario}')

print("-----------------------------")

print(funcionario[5])
salario = 1650
print(f'SALÁRIO LÍQUIDO= ${salario}') 
