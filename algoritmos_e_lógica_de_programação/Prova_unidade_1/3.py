'''(30) Construa um programa em Python que leia o nome e a carga horária de uma
disciplina (em número de aulas), o número de faltas e as 3 notas de um aluno nesta
disciplina. O programa deve calcular a média aritmética final deste aluno. Considere
que cada nota pode ir de 0 até 10.0. O programa também deve calcular a frequência
do aluno. O programa deve mostrar, além do nome e da carga horária da disciplina,
a mensagem “Reprovado por Falta” caso o aluno não tenha atingido pelo menos
75% da frequência, independente da média que atingiu. Caso não tenha sido
reprovado por falta, o programa deve mostrar também o valor da média e uma
mensagem de "Aprovado", caso a média seja igual ou superior a 7.0; “Final”, caso a
média seja igual ou superior a 4.0 e menor que 7.0, ou a mensagem "Reprovado",
se a média for menor que 4.0.'''

nome = str(input("Qual a nomeclatura da disciplina? "))
carga = int(input("Qual o total de aulas? "))
faltas = int(input("Quantas são faltas totais? "))
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

media = (nota1 + nota2 + nota3)/3

frequencia = ((carga - faltas)* 100)/carga

print(f'Disciplina: {nome}.')
print(f'Carga horária: {carga} aulas.')
print(f'A frequência é deste aluno é de {frequencia}%')

if frequencia < 75: 
    print("Reprovado por Falta")
elif frequencia >= 75:
    if media >= 7:
        print(f'Média de {media}')
        print("Aprovado")
    elif media < 7 and media >= 4:
        print(f'Média de {media}')
        print("Final")
    elif media < 4:
        print(f'Média de {media}')
        print("Reprovado")
