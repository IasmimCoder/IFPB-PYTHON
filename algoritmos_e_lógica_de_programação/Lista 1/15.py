#A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco)
# prestações sem juros. Faça um programa que receba um valor de uma compra
# e mostre o valor das prestações.

total_compra = float(input("Qual o valor total da compra? R$"))
quant_prest = int(input("Em quantas prestações você deseja dividir? "))
prest = total_compra/quant_prest

print("Suas prestações são de R$",prest,"sem juros!!")
