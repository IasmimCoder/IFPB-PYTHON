#Faça um programa que peça a cotação do dólar turismo, a quantidade de dólares a
# serem comprados e imprima quanto você vai precisar em reais, dado que o IOF
# é de 1,1% e o spread da casa de câmbio (taxa que ela ganha em cima da
# cotação) é de 2,5%.

cotacao = float(input("Digite a cotação do dólar turismo: "))
dolar_a_comprar = float(input("Quantos doláres você deseja comprar? "))

iof = (dolar_a_comprar * 0.011) * cotacao
spread = (dolar_a_comprar * 0.025) * cotacao

reais = (dolar_a_comprar * cotacao) + iof + spread

print(f'Para comprar {dolar_a_comprar} doláres, somado aos impostos, você irá precisar de R${reais}.')
