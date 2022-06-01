matriz = []
soma = 0.0
linha_operação = int(input())
operação = str(input())

#Faz a matriz linha por linha
for linha in range(12):   
    linha = []

    #adiciona os elementos na linha (colunas)
    for coluna in range(12):
        number = float(input())
        linha.append(number)
    matriz.append(linha)

#percorre a matriz para chegar na linha operação.
for linha in range(12):
    for coluna in range(12):
        if linha == linha_operação:
            soma += matriz[linha][coluna]

if operação == "S":
    print(f"{soma:.1f}")
elif operação == "M":
    soma = soma/12
    print(f"{soma:.1f}")
