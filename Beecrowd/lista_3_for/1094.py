'''
Experiências

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. 
Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. 
Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. 
Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.


'''

n = int(input())

c = 0
r = 0
s = 0 

for i in range(n):
    quant, animal = input().split()
    if animal == "C":
        c += int(quant)
    elif animal == "R":
        r += int(quant)
    elif animal == "S":
        s += int(quant)

total = c + r + s

porc_c = (c/total)*100
porc_r = (r/total)*100
porc_s = (s/total)*100

print(f"Total: {total} cobaias")
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {porc_c:.2f} %')
print(f'Percentual de ratos: {porc_r:.2f} %')
print(f'Percentual de sapos: {porc_s:.2f} %')



