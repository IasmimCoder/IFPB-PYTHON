#Escreva um programa que leia o nome de um aluno e as notas das três provas
# que ele obteve no semestre. No final informe o nome do aluno e a sua média
# (aritmética). Exemplo de formatação da saída: Nome do aluno: Fumizeldo
# Media de Fumizeldo é: 8,5.

nome = input("Informe o nome completo do aluno: ")
prova1 = float(input("Qual a sua primeira nota? "))
prova2 = float(input("Qual a sua segunda nota? "))
prova3 = float(input("Qual a sua terceira nota? "))

media = (prova1 + prova2 + prova3)/3

print ("Aluno(a): ",nome,".", "Média: ",media)
