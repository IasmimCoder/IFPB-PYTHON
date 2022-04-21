#Faça um programa que solicite ao usuário que informe a área de um terreno em
# metros quadrados e mostre as áreas correspondentes em acres, pés quadrados
# e hectares.

area_metros = float(input("Informe a área do terreno em metros quadrados: "))

acre = 4046.86 * area_metros
pés = 10.764 * area_metros
hectares =  area_metros / 10000

print(f'{area_metros} metros quadrados equivalem à {acre} acres quadrados.')
print(f'Equivale também à {pés} pés quadrados')
print(f'E também é igual à {hectares} hectares quadrados.')
