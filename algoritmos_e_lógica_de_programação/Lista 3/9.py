'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar M
(matutino), V (vespertino) ou N (noturno). Imprima a mensagem "Bom Dia!", "Boa
Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

letra = str(input("Digite o seu turno (M/V/N):"))

if (letra == "M") or (letra == "m"):
    print("Bom dia!")
elif (letra == "V") or (letra == "v"):
    print("Boa tarde!")
elif (letra == "N") or (letra == "n"):
    print("Boa noite!")
else:
    print("Valor Inválido!")