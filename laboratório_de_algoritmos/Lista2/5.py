'''
A PassaAlcool70 tem três tipos de funcionários: gerente (GER), vendedor (VEN) e
estoquista (EST). Faça um programa para mostrar o salário de um funcionário, sabendo
que o salário bruto do gerente é R$2300,00, do vendedor é R$2000,00 e do estoquista
é R$1650,00. O imposto de renda é retido na fonte e é de 12%, porém valores até
R$1700,00 são isentos. Perceba que a alíquota só incide sobre o valor que extrapola a
faixa de isenção.
'''
funcionario = str(input("(GER) para gerente, (VEN) para vendedor e (EST) para estoquista: ")).lower()
salario = 0

if funcionario == "ger":
    salario = 2300 - (2300*0.12)
elif funcionario == "ven":
    salario = 2000 - (2000*0.12)
elif funcionario == "est":
    salario = 1650

print(f'O salário deste funcinário é de {salario}.')

