'''A PassaAlcool70 está bombando! Mascariane, como forma de agradecimento e de
incentivo aos funcionários, dá um bônus de 13% sobre o salário bruto sempre que a
meta do mês é batida. Para informatizar isso, o programa deve perguntar se a meta foi
batida e implementar o bônus aos salários, em caso afirmativo. Preste atenção ao
imposto.'''

meta = str(input("A meta foi atingida? (Yes or No): ")).lower()

while meta != "yes" and meta != "no":
    meta = str(input("A meta foi atingida? (Digite apenas 'yes' ou 'no'): ")).lower()


if meta == "yes":
    funcionario = str(input("(GER) para gerente, (VEN) para vendedor e (EST) para estoquista: ")).lower()
    salario = 0
    bonus = 0.13

    if funcionario == "ger":
        salario_atual = 2300
        bonus = salario_atual * bonus
        imposto = (salario_atual + bonus) * 0.12
        salario_atual = (salario_atual + bonus) - imposto
    elif funcionario == "ven":
        salario_atual = 2000
        bonus = salario_atual * bonus
        imposto = (salario_atual + bonus) * 0.12
        salario_atual = (salario_atual + bonus) - imposto
    elif funcionario == "est":
        salario_atual = 1650
        bonus = salario_atual * bonus
        imposto = 0
        salario_atual = (salario_atual + bonus) - imposto
    print(f'O novo salário deste funcinário é de {salario_atual}.')

if meta == "no":
    print("Os salários continuam os mesmos.")

