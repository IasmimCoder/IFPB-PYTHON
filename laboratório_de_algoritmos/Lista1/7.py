#Faça um programa que peça ao usuário dois números inteiros e um número real.
#Calcule e mostre:
#o o produto do dobro do primeiro com metade do segundo.
#o a soma do triplo do primeiro com o terceiro.
#o o terceiro elevado ao cubo.

number1= int(input("Digite um número inteiro: "))
number2= int(input("Digite outro número inteiro: "))
number3= float(input("Agora, digite um número real: "))

calc1 = (number1*2)*(number2/2)
print(f'O produto do dobro do primeiro número com metade do segundo é {calc1}.')

calc2= (number1*3) + number3
print(f'A soma do triplo do primeiro número com o terceiro é {calc2}.')

calc3 = number3**3
print(f'O terceiro número elevado ao cubo é {calc3}.')
