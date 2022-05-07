'''Aumento
A empresa realmente é lucrativa, e Mascariane acha justo reajustar os salários dos
seus funcionários de vez em quando. Ela já quer deixar o reajuste informatizado para
que quando ocorra, ela rapidamente consiga calcular para cada funcionário.
Ela quer testar um modelo em que o reajuste de cada cargo aumente a cada ano: o
gerente começaria ganhando um reajuste de 3%, o vendedor de 2% e o estoquista de
1,5% no primeiro ano. A partir de então, a cada ano, cada cargo aumentaria seu reajuste
em 1%. Por exemplo, no segundo ano o gerente teria um reajuste de 4%, no terceiro de
5% e assim por diante.
Para verificar a viabilidade desse modelo, ela precisa projetar qual seria o impacto
nos cofres da empresa. Para isso, faça um programa que peça ao usuário que informe
o código do funcionário (GER, VEN, EST), calcule e imprima o salário projetado com o
reajuste de cada ano, a porcentagem do reajuste acumulada (em relação ao salário
atual) a cada ano e o total que será pago ao funcionário a cada ano. Tudo isso por 10
anos. Ao final, imprimir o total que a empresa precisará pagar ao funcionário ao longo
dos 10 anos.
O programa deve permitir a consulta a vários funcionários em sequência, até que o
usuário informe que não quer mais consultar nenhum.
PS: perceba que não haverá desconto de IR aqui, pois a empresa retém o valor, mas
repassa à Receita Federal.'''

consulta = str(input("Deseja consultar o salário algum funcionário? (yes/y or no/n)")).lower().strip()[0]

# também funciona: while consulta not in 'yn'
while consulta != "y" and consulta != "n":
    consulta = str(input("Deseja consultar o salário algum funcionário? Digite apenas 'yes/y' or 'no/n': ")).lower().strip()[0]

while consulta[0] == "y":


    funcionario = str(input("(GER) para gerente, (VEN) para vendedor e (EST) para estoquista: ")).lower().strip()

    while funcionario != "ger" and funcionario != "ven" and funcionario != "est":
        funcionario = str(input("(Digite apenas (GER) para gerente, (VEN) para vendedor e (EST) para estoquista: ")).lower().strip()

    salario = 0
    salario_inicial = 0
    reajuste = 0
    total_pago = 0
    reajuste_acumulado = 0

    if funcionario == "ger":
        salario_inicial = 2300 
    elif funcionario == "ven":
        salario_inicial = 2000 
    elif funcionario == "est":
        salario_inicial = 1650

    while funcionario == "ger": 
        reajuste = 0.03
        salario = salario_inicial + (salario_inicial * reajuste)
        print(f"O salário, com o reajuste de 3%, é de ${salario:.2f}")
        funcionario = " "
        reajuste_acumulado = reajuste
        reajuste = 0.01

        for i in range(2, 10+1):
            salario += (salario * reajuste)
            reajuste_acumulado += reajuste
            print(f"No {i}º ano o salário será de ${salario:.2f}")
            print(f"Reajuste acumulado: {(reajuste_acumulado * 100):.2f}%")
            total_pago += salario
        print(f"O total a ser pago em 10 anos para este funcionário é ${total_pago:.2f}.")

    while funcionario == "ven":
        reajuste = 0.02
        salario = salario_inicial + (salario_inicial * reajuste)
        print(f"O salário, com o reajuste de 2%, é de ${salario:.2f}")
        funcionario = " "
        reajuste_acumulado = reajuste
        reajuste = 0.01

        for i in range(2, 10+1):
            salario += (salario * reajuste)
            reajuste_acumulado += reajuste
            print(f"No {i}º ano o salário será de ${salario:.2f}")
            print(f"Reajuste acumulado: {(reajuste_acumulado * 100):.2f}%")
            total_pago += salario
        print(f"O total a ser pago em 10 anos para este funcionário é ${total_pago:.2f}.")

    while funcionario == "est":
        reajuste = 0.015
        salario = salario_inicial + (salario_inicial * reajuste)
        print(f"O salário, com o reajuste de 1.5%, é de ${salario:.2f}")
        funcionario = " "
        reajuste_acumulado = reajuste
        reajuste = 0.01

        for i in range(2, 10+1):
            salario += (salario * reajuste)
            reajuste_acumulado += reajuste
            print(f"No {i}º ano o salário será de ${salario:.2f}")
            print(f"Reajuste acumulado: {(reajuste_acumulado * 100):.2f}%")
            total_pago += salario
        print(f"O total a ser pago em 10 anos para este funcionário é ${total_pago:.2f}.")

    consulta = str(input("Deseja consultar o salário algum funcionário novamente? (yes/y or no/n)")).lower().strip[0]

    while consulta != "y" and consulta != "n":
        consulta = str(input("Deseja consultar o salário algum funcionário? Digite apenas 'yes/y' or 'no/n': ")).lower().strip[0]

print("Bom trabalho!")
