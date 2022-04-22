'''A sequência de Fibonacci é uma famosa sequência de números determinada pela
seguinte lei de formação:
• Os dois primeiros termos da sequência são os números 0 e 1;
• Do terceiro termo em diante, cada um é determinado pela soma dos dois
anteriores.

Veja: 0+1=1, 1+1=2, 2+1=3, 3+2=5 e assim sucessivamente. Assim, o início da
sequência é: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...). Sabendo disso, escreva um programa
em Python que lê do usuário um valor N e retorna uma lista contendo os N primeiros
termos da sequência de Fibonacci.'''

n = int(input("Digite um valor n: "))
termo_a = 0
termo_b = 1
print(termo_a)
print(termo_b)
for x in range(1, n+1):
    termo_c = termo_a + termo_b
    termo_a = termo_b
    termo_b = termo_c
    print(termo_c)
