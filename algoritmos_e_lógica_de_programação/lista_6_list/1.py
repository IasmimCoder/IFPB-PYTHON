'''
Escreva um programa para pedir ao usuário duas listas de 15 componentes inteiros
distintos cada e determinar o conjunto interseção para os conjuntos lidos. Imprima a
lista contendo conjunto interseção, ao final.
'''

lista_1 = []
lista_2 = []
intersecção = []
elemento_lista_1 = "0"
ordem = 0

for i in range(1, 6):
    lista_1.append(int(input(f"Digite {i}º número inteiro do primeiro conjunto: ")))

for i in range(1, 6):
    lista_2.append(int(input(f"Digite {i}º número inteiro do segundo conjunto: ")))

#percorrendo lista 
# for elemento in lista_1:
#     print(elemento)

#verificação se o elemento X está contido na lista Y.
# x = [0, 1, 2, 3]
# if 2 in x:
#     print("Contido")


for elemento in lista_1:
    ordem += 1
    print(f'O {ordem}º elemento do primeiro conjunto é {elemento}.')

    if elemento in lista_2:
        print(f"Este elemento '{elemento}' está contido também na lista 2.")

        intersecção.append(elemento)

print(f'O conjunto intersecção é {intersecção}')
