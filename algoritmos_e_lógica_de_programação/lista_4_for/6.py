'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de multiplicar de
qualquer número inteiro entre 0 a 10. O usuário deve informar de qual número ele
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo (se ele informar
5):'''

number = int(input("De qual número você deseja ver a tabuada? "))
print(f'Tabuada de {number}:')

for x in range(11):
    tabuada = number*x
    print(f"{number} x {x} = {tabuada}")
