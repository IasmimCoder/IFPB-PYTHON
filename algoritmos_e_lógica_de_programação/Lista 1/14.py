#Escreva um programa que calcule com quantos litros de gasolina é preciso
# abastecer um veículo, dada a distância que se deseja percorrer e a quantidade
# de quilômetros que o veículo faz por litro.

km_lt = float(input("Quantos quilômetros seu veículo faz por litro?"))
distancia = float(input("Qual distância deseja percorrer? (KM)"))
quant_lit = distancia/km_lt

print("Você precisa abastecer",quant_lit,"litros para percorrer",distancia,"quilômetros.")
