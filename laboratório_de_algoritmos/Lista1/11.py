#Faça um programa que peça ao usuário a média e a nota da final e calcule e mostre sua
#média final. Lembrando que a média final é composta de 60% da média e 40%da nota da final.

media = float(input("Digite a média: "))
nota_final = float(input("Digite a nota final: "))

media_final = media * 0.6 + nota_final * 0.4
print(f'A média final é, portanto, {media_final}.')
