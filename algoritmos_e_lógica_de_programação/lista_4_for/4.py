'''Faça um programa que receba dois números do usuário e mostre quantos números
entre os dois passados (incluindo ambos) são pares e divisíveis por 9.'''

qtd_numbers = 0 

for x in range(2):
    number = int(input("Digite um numéro inteiro: "))

    if number %2 == 0 and number % 9 == 0:
        qtd_numbers += 1

if qtd_numbers == 1:
    print(f"APENAS UM número é par e dívisivel por 9.")
elif qtd_numbers == 2: 
    print(f'AMBOS são pares e divisíveis por 9!')
