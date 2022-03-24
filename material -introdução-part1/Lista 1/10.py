#Escreva um programa que efetue a apresentação do valor da conversão em real
# (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar ao usuário o
# valor da cotação do dólar e também a quantidade de dólares que ele deseja converter.

valor_dolar = float(input("Quantos doláres você deseja converter? "))
cotacao = float(input("Qual o valor da cotação do dolár? "))
valor_real = valor_dolar*cotacao

print("Você tem R$",valor_real,"convertidos.")
