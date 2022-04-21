#15. Faça um programa que calcule e apresente o valor do volume de uma lata de
#óleo, dado seu raio e sua altura. (Pi = 3.14)

raio = float(input("Qual o raio da sua lata de óleo? "))
altura = float(input("E qual a altura da sua lata de óleo? "))
volume = raio **2 * 3.14 *altura
print(f'O volume da sua lata de óleo é {volume}.')