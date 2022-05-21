'''(20) Faça um programa em Python que receba a temperatura média de cada mês
do ano em Monteiro e armazene-as em uma lista. O usuário já informará as
temperaturas na ordem correta dos meses (Janeiro, Fevereiro, ..., Dezembro). Após
isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima
da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: Janeiro,
Fevereiro, . . .).'''

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas = []

soma = 0

mes = 0

for i in range(0, 12):
    temperaturas.append(float(input(f"Digite a temperatura média do {i+1}º mês: ")))
    soma += temperaturas[i]
    
media_anual = soma/12

for temperatura in temperaturas:
    if temperatura > media_anual:
        print(f"A temperatura do mês de {meses[mes]} foi acima da média, com {temperaturas[mes]}°.")
    mes += 1


