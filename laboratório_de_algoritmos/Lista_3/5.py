'''5. Bônus
A PassaAlcool70 está bombando! Mascariane, como forma de agradecimento e de
incentivo aos funcionários, dá um bônus de 13% sobre o salário bruto sempre que a
meta do mês é batida. Para informatizar isso, o programa deve perguntar se a meta foi
batida e implementar e mostrar o bônus aos salários de todos os funcionários, em caso
afirmativo. Preste atenção ao imposto.'''

meta = str(input("A meta foi atingida? (yes or no): ")).lower().strip()[0]

while meta != "y" and meta != "n":
    meta = str(input("A meta foi atingida? (Digite apenas 'yes' ou 'no'): ")).lower().strip()[0]

if meta == "y":
    funcionario = ["Gerente", "Vendedor 1", "Vendedor 2", "Vendedor 3", "Estoquista 1", "Estoquista 2"]

    print(funcionario[0])
    salario_bruto = 2300 
    bonus = salario_bruto * 0.13
    novo_salario_bruto = salario_bruto + bonus
    salario_liquido = novo_salario_bruto - (novo_salario_bruto*0.12)
    print(f'NOVO SALÁRIO LÍQUIDO= ${salario_liquido}')

    print("-----------------------------")

    print(funcionario[1])
    salario_bruto = 2000
    bonus = salario_bruto * 0.13
    novo_salario_bruto = salario_bruto + bonus
    salario_liquido = novo_salario_bruto - (novo_salario_bruto*0.12)
    print(f'NOVO SALÁRIO LÍQUIDO= ${salario_liquido}')

    print("-----------------------------")

    print(funcionario[2])
    salario_bruto = 2000
    bonus = salario_bruto * 0.13
    novo_salario_bruto = salario_bruto + bonus
    salario_liquido = novo_salario_bruto - (novo_salario_bruto*0.12)
    print(f'NOVO SALÁRIO LÍQUIDO= ${salario_liquido}')

    print("-----------------------------")

    print(funcionario[3])
    salario_bruto = 2000 
    bonus = salario_bruto * 0.13
    novo_salario_bruto = salario_bruto + bonus
    salario_liquido = novo_salario_bruto - (novo_salario_bruto*0.12)
    print(f'NOVO SALÁRIO LÍQUIDO= ${salario_liquido}')
    
    print("-----------------------------")

    print(funcionario[4])
    salario_bruto = 1650
    bonus = salario_bruto * 0.13
    novo_salario_bruto = salario_bruto + bonus 
    salario_liquido = novo_salario_bruto 
    
    if novo_salario_bruto >= 1700: 
        salario_liquido = novo_salario_bruto - (novo_salario_bruto*0.12)
    
    print(f'NOVO SALÁRIO LÍQUIDO= ${salario_liquido}')
    print("-----------------------------")

    print(funcionario[5])
    salario_bruto = 1650
    bonus = salario_bruto * 0.13
    novo_salario_bruto = salario_bruto + bonus 
    salario_liquido = novo_salario_bruto 
    
    if novo_salario_bruto >= 1700: 
        salario_liquido = novo_salario_bruto - (novo_salario_bruto*0.12)
    
    print(f'NOVO SALÁRIO LÍQUIDO= ${salario_liquido}')
    print("-----------------------------")
