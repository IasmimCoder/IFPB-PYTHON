#Uma empresa quer dar um bônus de Natal (em dezembro, claro) para seus
# empregados que será 60% do cálculo médio do salário de trabalho.
# Considerando que todos na empresa ganhem um mesmo valor de salário,
# elabore um programa que receba a entrada do salário e imprima o valor do bônus
# de Natal e o valor a ser depositado na conta de cada empregado em dezembro.

#receba a entrada do salário
salario = float(input("Informe o salário dos empregados: "))

# imprima o valor do bônus de Natal
bonus = (salario * 6)/10 
print("O bônus deste Natal é de $",bonus)
#Ou: (salario* 60)/100
#Também: salario*0,6

#imprima o valor a ser depositado na conta de cada empregado em dezembro.
sal_total = salario + bonus 
print("Os empregados receberão $",sal_total,"de salário total no Natal!")
