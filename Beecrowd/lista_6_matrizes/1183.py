matriz = []
soma = 0
contador = 0
operação = str(input())

#Faz a matriz linha por linha
for linha in range(12):   
    linha = []

    #adiciona os elementos na linha (colunas)
    for coluna in range(12):
        number = float(input())
        linha.append(number)
    matriz.append(linha)

index_coluna = 0
for x in range(len(matriz)-1): #percorre a linha 11 vezes (matriz 12x12)
    index_coluna += 1
    for y in range(index_coluna, len(matriz)):
        soma += (matriz[x][y])
        contador += 1


if operação == "S":
    print(f"{soma:.1f}")

if operação == "M":
    media = soma/contador
    print(f"{media:.1f}")
