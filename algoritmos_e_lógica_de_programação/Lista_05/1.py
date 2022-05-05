'''
Faça um programa que peça uma nota (float), entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário informe
um valor válido. Imprima a nota válida digitada ao final, dizendo se com a nota o
usuário foi aprovado ou não (aprovado >=7.0).
'''

nota = float(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota apenas de 0 a 10: "))

if nota >= 7.0:
    print(f"Aprovado(a) com a nota de {nota}.")
else: 
    print(f'Reprovado(a) com a nota de {nota}.')
    