'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se
o conceito for D ou E.
'''

nota_1 = float(input("Digite a 1º nota: "))
nota_2 = float(input("Digite a 2º nota: "))
media = (nota_1 + nota_2)/2

print(f'1ª nota: {nota_1}')
print(f'2ª nota: {nota_2}')
print(f'Média: {media}')

if ((media >= 9)):
    print("Conceito: A")
    print("APROVADO")
elif ((media >= 7.5) and (media < 9)):
    print("Conceito: B")
    print("APROVADO")
elif ((media >= 6) and (media < 7.5)):
    print("Conceito: C")
    print("APROVADO")
elif ((media >= 4) and (media < 6)):
    print("Conceito: D")
    print("REPROVADO")
elif (media < 4):
    print("Conceito: E")
    print("REPROVADO")
