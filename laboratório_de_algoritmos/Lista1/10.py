#Faça um programa que calcule e mostre a média de um aluno em uma disciplina
# em ADS. Para isso, o usuário deve informar as três notas do aluno.

nota1= float(input("Informe sua nota 1: "))
nota2= float(input("Informe sua nota 2: "))
nota3= float(input("Informe sua nota 3: "))

media = (nota1 + nota2 +nota3)/3

print(f'A média deste aluno é {media}.')
