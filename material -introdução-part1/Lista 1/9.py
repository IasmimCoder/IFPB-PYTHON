#Escreva um programa que peça ao usuário dois números naturais para as
# variáveis A e B, e efetue as trocas dos valores de forma que a variável A passe
# a possuir o valor da variável B e a variável B passe a possuir o valor da variável
# A. Apresentar os valores trocados.

a = int(input("Digite um número de 0 a 10 para a variavél A: "))
b = int(input("Agora, digite um número de 0 a 10 para a variavél B: "))

print("Ok. A =",a,"e B =",b,"")

"""aux = a
a = b
b = aux
"""
a, b = b, a

print("Novos valores: A =",a,"e B =",b,"")
