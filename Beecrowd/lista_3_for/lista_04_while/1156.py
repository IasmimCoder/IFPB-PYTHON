'''
Sequência S II

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.

'''
 
#s = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
s = 1

valor_a = 2
valor_b = 3

while valor_b  < 39:
    s = s + (valor_b/valor_a)

    valor_a *= 2
    valor_b += 2

print(f'{s:.2f}')
