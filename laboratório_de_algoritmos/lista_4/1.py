'''A vida de empresária não é fácil. São milhares de problemas a resolver com
clientes, funcionários, banco, etc; melhorias a implantar; mercadorias a solicitar
e conferir; e por aí vai.
Para que Mascariane possa dar conta de todos as pendências em tempo
hábil, ela desenvolveu uma técnica para se organizar. A cada início de dia, ela
verifica as pendências a serem resolvidas, priorizando as pendências mais
urgentes para resolver no dia e deixando as demais para depois. Ela sempre
fazia isso em listas escritas à mão em papel, mas agora você pode ajudá-la a
informatizar essa organização com seus conhecimentos de programação.
Faça um programa que peça a Mascariane uma pendência (uma string) e a
insira em uma lista de pendências. Mascariane vai informar todas as pendências,
mas nem você nem ela sabem antecipadamente quantas são. 
Quando ela terminar de informar todas as pendências, elas serão inseridas 
em uma das duas pilhas: urgentes ou normais. Para isso, percorra a lista de pendências,
informando cada pendência a Mascariane e perguntando se ela vai resolvê-la
hoje ou deixar para depois. Se Mascariane disser que vai resolver a pendência
hoje, ela deve ser inserida na pilha de urgentes. Se não, na pilha de normais. Ao
final, mostre a primeira pendência urgente à Mascariane, já a tirando da pilha.
Daí, diga a Mascariane que quando ela resolver, digite a palavra “Próxima”.
Repita este ciclo até que a pilha tenha se encerrado ou que Mascariane informe
que o dia de trabalho terminou. 
Se o dia de trabalho tiver terminado e a pilha de urgências não estiver 
vazia, insira as pendências urgentes na pilha de pendências normais, 
pois ficarão para o outro dia e ela pode reanalisar se ainda serão 
tão urgentes amanhã (podem ter chegado pendências ainda mais
urgentes, ufa!).'''


# Faça um programa que peça a Mascariane uma pendência (uma string) e a
# insira em uma lista de pendências. Mascariane vai informar todas as pendências,
# mas nem você nem ela sabem antecipadamente quantas são.

lista_de_pendencias = []

ordem = 0

novas_pendencias = str(input("Deseja adicionar pendências hoje? 'y'/'n': ")).lower().strip()[0]

while novas_pendencias == "y":
    ordem += 1
    lista_de_pendencias.append(str(input(f"+ {ordem}º pendência: ")))
    novas_pendencias = str(input("Deseja adicionar mais pendências? 'y'/'n': ")).lower().strip()[0]

    while novas_pendencias != "y" and novas_pendencias != "n":
        novas_pendencias = str(input("Deseja adicionar mais pendências? Digite apenas: 'y'/'n': ")).lower().strip()[0]

# Quando ela terminar de informar todas as pendências, elas serão inseridas em uma das duas
# pilhas: urgentes ou normais. Para isso, percorra a lista de pendências,informando cada 
# pendência a Mascariane e perguntando se ela vai resolvê-la hoje ou deixar para depois.
# Se Mascariane disser que vai resolver a pendência hoje, ela deve ser inserida na pilha 
# de urgentes. Se não, na pilha de normais.

urgentes = []
normais = []
prioridade = 0
for pendencia in lista_de_pendencias:
    print(f'Irá resolver a pendência "{pendencia}" hoje ou depois?')
    prioridade = int(input("Digite [1] para hoje e [2] para depois: "))

    while prioridade != 1 and prioridade != 2:
        prioridade = int(input("Digite apenas [1] para hoje e [2] para depois: "))

    if prioridade == 1:
        urgentes.append(pendencia)
    if prioridade == 2:
        normais.append(pendencia)

# Ao final, mostre a primeira pendência urgente à Mascariane, já a tirando da pilha.
# Daí, diga a Mascariane que quando ela resolver, digite a palavra “Próxima”.
# Repita este ciclo até que a pilha tenha se encerrado ou que Mascariane informe
# que o dia de trabalho terminou. 

solve = "próxima"

ordem = 0

while solve == "próxima" and len(urgentes) >= 1:
    ordem += 1
    tarefa = urgentes.pop()
    print(f'{ordem}º pendência urgente: {tarefa}')

    solve = str(input("Quando resolver, digite 'próxima'. Se o dia de trabalho acabou, digite 'fim': ")).lower().strip()

    while solve != "próxima" and solve != "fim":
        solve = str(input("Digite apenas 'próxima' ou 'fim': ")).lower().strip()

# Se o dia de trabalho tiver terminado e a pilha de
# urgências não estiver vazia, insira as pendências urgentes na pilha de
# pendências normais, pois ficarão para o outro dia e ela pode reanalisar se ainda
# serão tão urgentes amanhã (podem ter chegado pendências ainda mais
# urgentes, ufa!).

if solve == "fim" and len(urgentes) >= 1:
    for pendencia in urgentes:
        normais.append(pendencia)
    print(f'Seu dia de trabalho acabou. Todas as suas pendências estão na lista de prioridade "normal".')
    print(f"Pendências normais: {normais}")


# #se a pilha de urgentes for concluída e o dia de trabalho não tiver acabado:
# ordem = 0

# while len(urgentes) == 0 and len(normais) >= 1 and solve != "fim":
#     ordem += 1
#     tarefa = normais.pop()
#     print(f'{ordem}º pendência normal: {tarefa}')

#     solve = str(input("Quando resolver, digite 'próxima'. Se o dia de trabalho acabou, digite 'fim': ")).lower().strip()

#     while solve != "próxima" and solve != "fim":
#         solve = str(input("Digite apenas 'próxima' ou 'fim': ")).lower().strip()