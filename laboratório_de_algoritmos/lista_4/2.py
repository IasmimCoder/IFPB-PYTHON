'''
Você está sabendo do babado que teve lá na PassaAlcool70 ontem?
Confusão graaaande entre uns clientes porque uns chegaram depois e foram
atendidos primeiro. Não é pra menos, né? O problema é que o vendedor era
novato e se embananou todo para fazer os atendimentos e todos os
procedimentos de venda. E olha que seus programas já ajudam muito, hein?

Depois do bafafá, Mascariane resolveu pedir que você implantasse um
sistema para controlar as filas na loja. Como Mascariane gosta de seguir as leis,
ela quer que você implante o atendimento prioritário a deficientes, idosos,
grávidas e puérperas. Só que ela não quer um caixa prioritário e outro para
atendimento normal, para evitar que algum caixa fique ocioso enquanto outro
com filas grandes.

Para isso, você vai fazer um programa Python que pergunte o nome do
cliente e se ele é prioritário por lei quando ele for para o caixa. Você vai criar
duas filas, uma de atendimento prioritário e outra de atendimento normal. Se o
cliente for prioritário, você (obviamente!) coloca o nome dele na fila prioritária, se
não, na fila normal.

O atendimento se dará da seguinte forma: a cada atendimento prioritário, dois
atendimentos normais são realizados. Se uma das filas estiver vazia, claro que
será chamado alguém da fila que tiver clientes. O atendimento para quando
ambas as filas estiverem vazias.
É bom testar o programa antes de implantar na loja. Então, para saber se seu
programa está funcionando bem, faça uma simulação inserindo 3 clientes
prioritários e 8 normais e iniciando o atendimento de todos, até as duas filas
ficarem vazias.
'''

fila_normal = []
fila_prioritaria = []

clientes = str(input("Deseja adicionar novos clientes? 'y'/'n': ")).lower().strip()[0]

while clientes != "y" and clientes != "n":
    clientes = str(input("Deseja adicionar novos clientes? Digite apenas 'y'/'n': ")).lower().strip()[0]


while clientes == "y":

    nome = str(input("Digite o nome do cliente: "))
    prioritario = str(input("O cliente é prioritário por direito? 'y'/'n': ")).lower().strip()[0]
   
    if prioritario == "y":
        fila_prioritaria.append(nome)
    elif prioritario == "n":
        fila_normal.append(nome)

    clientes = str(input("Deseja adicionar novos clientes? 'y'/'n': ")).lower().strip()[0]

    while clientes != "y" and clientes != "n":
        clientes = str(input("Deseja adicionar novos clientes? Digite apenas 'y'/'n': ")).lower().strip()[0]

atendimento = []

while len(fila_normal) >= 1 or len(fila_prioritaria) >= 1:
    preferencial = fila_prioritaria.pop(0)
    atendimento.append(preferencial)

    for i in range(2):
        comum = fila_normal.pop(0)
        atendimento.append(comum)

print(f'Atendimento: {atendimento}')