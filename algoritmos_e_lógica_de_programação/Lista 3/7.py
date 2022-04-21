'''
Faça um programa que leia 3 números e calcule a média ponderada entre eles.
Considere que o maior número recebe peso 5 e os outros dois recebem peso
2,5.
'''

valor1 = int(input("Digite um número inteiro: "))
valor2 = int(input("Digite outro número inteiro: "))
valor3 = int(input("Digite mais um número inteiro: "))
media = 0

if ((valor1 > valor2 >= valor3) or (valor1 > valor3 > valor2)):
    media = (valor1 * 5 + valor2 * 2.5 + valor3 * 2.5)/10
elif ((valor2 > valor1 >= valor3) or (valor2 > valor3 > valor1)):
    media = (valor2 * 5 + valor1 * 2.5 + valor3 * 2.5)/10
elif ((valor3 > valor2 >= valor1) or (valor3 > valor1 > valor2)):
    media = (valor3 * 5 + valor1 * 2.5 + valor2 * 2.5)/10

print(f'A média ponderada é de {media}')
