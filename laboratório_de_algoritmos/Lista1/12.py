#Faça um programa que calcule e mostre a quantidade dinheiro gasta por um fumante. Dados: o número
#de anos que ele fuma, o número de cigarros fumados por dia e o preço de uma carteira de 20 cigarros.

anos = int(input("Quantos anos você consome cigarros? "))
dias_no_ano = 365 * anos
dia = int(input("Quantos cigarros você usa por dia? "))
preco_carteira = int(input("Qual o preço da carteira de cigarros que você mais usa frequentemente?"))
quantidade = int(input("Quantos cigarros sua carteira contém? "))
preco_unidade = preco_carteira/quantidade

valor = preco_unidade*dia*dias_no_ano
print(f'Você gastou ${valor} com cigarros nestes {anos} anos.')
