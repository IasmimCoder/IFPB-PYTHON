#Faça um programa que peça ao usuário sua altura e construa um algoritmo que 
# calcule e mostra seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58.

altura = float(input("Digite sua altura: "))
peso_ideal = (72.7*altura) - 58

print(f'O seu peso ideal é {peso_ideal}')
