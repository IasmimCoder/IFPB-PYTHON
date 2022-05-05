'''
Faça um programa que calcule e mostre a média aritmética de N notas. Faça todas
as validações necessárias.
'''
calc = str(input("Deseja calcular médias? ('yes/y' ou 'no/n'): ")).lower()[0]

while calc == "y": 

    qtd = int(input("Quantas notas deseja incluir? "))

    soma = 0

    for x in range(1, qtd+1):
        nota = float(input(f"Digite a {x}º nota: "))
        soma += nota

    media = soma / qtd 

    print(f"A média é de {media: .2f}")

    calc = str(input("Deseja calcular mais médias? ('yes/y' ou 'no/n'): ")).lower()[0]

if calc == "n":
    print("Ok!")

