'''
Faça um programa que peça dois números naturais, base e expoente, calcule e
mostre o primeiro número elevado ao segundo número. Não utilize a função de
potência da linguagem (**). Mostre uma mensagem caso os valores não sejam
naturais e continue pedindo até que o usuário informe valores válidos. Valide cada
valor separadamente.
''' 

number_1 = int(input("Digite um número natural para base: "))

while number_1 < 0: 
    print(f'{number_1} não é um número natural!')
    number_1 = int(input("Digite um número natural: "))

number_2 = int(input("Para o expoente, digite outro número natural: "))

while number_2 < 0: 
    print(f'{number_2} não é um número natural!')
    number_2 = int(input("Digite um número natural: "))

exponenciação = number_1 * number_1

for x in range(1, number_2-2):
    exponenciação += exponenciação * number_1 

print(f'O número {number_1} elevado ao número {number_2} é: exponenciação')
