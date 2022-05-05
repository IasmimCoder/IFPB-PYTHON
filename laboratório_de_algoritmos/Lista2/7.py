'''A empresa realmente é lucrativa, e Mascariane acha justo reajustar os salários dos seus
funcionários de vez em quando. Ela já quer deixar o reajuste informatizado para que
quando ocorra, ela rapidamente consiga calcular para cada funcionário. Ela quer testar
um modelo de aumento fixo a cada ano: o gerente ganha 8%, o vendedor 7% e o
estoquista 6,5%. O programa então deve perguntar se é para dar aumento. Caso seja,
pergunta o cargo do funcionário e seu salário bruto atual e retorna o novo salário bruto.'''

aumento = str(input("Deseja dar aumento? (Yes or No): ")).lower()

while aumento != "yes" and aumento != "no":
    aumento = str(input("A meta foi atingida? (Digite apenas 'yes' ou 'no'): ")).lower()


if aumento == "yes":
    funcionario = str(input("(GER) para gerente, (VEN) para vendedor e (EST) para estoquista: ")).lower()

    while funcionario != "ger" and funcionario != "ven" and funcionario != "est": 
        funcionario = str(input("Digite apenas (GER) para gerente, (VEN) para vendedor e (EST) para estoquista: ")).lower()

    salario_atual = float(input("Qual o salário bruto atual? "))
    bonus = 0

    if funcionario == "ger":
        bonus = salario_atual * 0.08
        salario_atual = salario_atual + bonus
    elif funcionario == "ven":
        bonus = salario_atual * 0.07
        salario_atual = salario_atual + bonus
    elif funcionario == "est":
        bonus = salario_atual * 0.065
        salario_atual = salario_atual + bonus

    print(f'O novo salário bruto deste funcinário é de {salario_atual}.')

if aumento == "no":
    print("Os salários continuam os mesmos.")