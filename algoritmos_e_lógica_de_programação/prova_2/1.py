'''(20) Escreva um programa em Python para informar se cidadãos já podem tomar a
vacina de gripe. O programa vai pedir ao usuário um número N que representa o
número de cidadãos a serem consultados, depois vai pedir ao usuário nome, idade
e se esse cidadão já se vacinou (‘Sim’ ou ‘Não’). O programa deve imprimir a
mensagem ‘Cidadão (nome do cidadão) pode se vacinar.’ sempre que um cidadão
informado tenha 12 anos ou mais e ainda não se vacinou. Nos demais casos, o
programa deve imprimir a mensagem ‘Cidadão (nome do cidadão) não pode se
vacinar.’.'''

n = int(input("Número de cidadãos a serem consultados: "))

for i in range(1, n+1):
    nome = str(input("Digite o nome do cidadão: "))
    idade = int(input("Qual a idade? "))

    vacina = str(input("Este já se vacinou? (sim/s ou não/n): ")).lower().strip()[0]

    if idade >= 12 and vacina == "n":
        print(f'Cidadão {nome} pode se vacinar.')
    else: 
        print(f'Cidadão {nome} não pode se vacinar.')
