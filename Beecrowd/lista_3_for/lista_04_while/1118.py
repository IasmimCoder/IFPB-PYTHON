'''Várias Notas Com Validação

Por Neilor Tonin, URI Brasil
Timelimit: 1

Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. 
Calcule e imprima a média semestral. 
O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). 
Cada nota deve ser validada separadamente.'''

novo_calculo = 1

while novo_calculo == 1: 
    nota_1 = float(input())

    while nota_1 < 0 or nota_1 > 10:
        print("nota invalida")
        nota_1 = float(input())

    nota_2 = float(input())

    while nota_2 < 0 or nota_2 > 10:
        print("nota invalida")
        nota_2 = float(input())

    media = (nota_1 + nota_2)/2
    print(f'media = {media:.2f}')

    novo_calculo = int(input("novo calculo (1-sim 2-nao)"))

    while novo_calculo < 1 or novo_calculo > 2:
        novo_calculo = int(input("novo calculo (1-sim 2-nao)"))


