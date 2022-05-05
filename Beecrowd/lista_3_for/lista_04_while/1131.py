'''Grenais

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. 
Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. 
Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. 
Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. 
Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". 
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.
'''

novo_grenal = 1
grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

while novo_grenal == 1:
    gols_inter,gols_gremio = input().split(" ")

    gols_inter = int(gols_inter)
    gols_gremio = int(gols_gremio)

    grenais += 1

    if gols_inter > gols_gremio: 
        vitorias_inter += 1 
    elif gols_gremio > gols_inter:
        vitorias_gremio += 1
    elif gols_inter == gols_gremio:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    novo_grenal = int(input())

if novo_grenal == 2:
    print(f"{grenais} grenais")
    print(f"Inter:{vitorias_inter}")
    print(f"Gremio:{vitorias_gremio}")
    print(f"Empates:{empates}")

    if vitorias_inter > vitorias_gremio:
        print("Inter venceu mais")
    elif vitorias_gremio > vitorias_inter:
        print("Gremio venceu mais")

    

