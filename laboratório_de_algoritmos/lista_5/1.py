'''1. Cadastro de clientes
Como você sabe, Mascariane está querendo fazer um cadastro de seus
clientes para que esses dados fiquem salvos e a ajude a tomar algumas decisões
como promoções, envio de e-mails, controle de cashback e etc.
Agora você vai fazer o cadastro de clientes em uma matriz. Cada linha da
matriz representará um cliente; cada coluna, uma informação do cliente.
Você vai fazer um programa em Python que permita que o vendedor
preencha essa matriz. O vendedor informará vários clientes em sequência até
que decida que terminou a tarefa. Para cada cliente, o programa irá solicitar ao
vendedor:
• Nome – fazer validação de pelo menos um sobrenome
• E-mail - fazer validação de presença do @
• Número de compras já realizadas
• Valor de cashback acumulado
Ao fim, o programa deve imprimir o cadastro de clientes, um cliente por linha.'''

matriz = []
informacoes = ['Nome', 'E-mail', 'Nº de compras realizadas', 'Valor de cashback acumulado']
cliente_novo = "y"
index_cliente = 0
index_info = 0

while cliente_novo == "y":
    linha = []
    index_cliente += 1

    print("----"*4)
    print(f"{index_cliente}º CLIENTE NOVO")
    print("----"*4)
    for j in range(4):
        print(f"Informe o {informacoes[index_info]}:")
        informacao = input()

        linha.append(informacao)
        index_info += 1 
    matriz.append(linha)
    index_info = 0

    cliente_novo = str(input("Deseja adicionar mais clientes? ('y'/'n'): ")).lower().strip()[0]
    
    while cliente_novo != "y" and cliente_novo != "n":
        cliente_novo = str(input("Deseja adicionar mais clientes? ('y'/'n'): ")).lower().strip()[0]


for cliente in matriz:
    print(cliente)

# print(f"Nº |\t {informacoes[0]}\t{informacoes[1]}\t\t{informacoes[2]}\t{informacoes[3]}")
# for index, cliente in enumerate(matriz): 
#     print(index+1, end="  |  ")
#     for dado in cliente:
#         if dado == cliente[-1]:
#             print(end="\t\t")
#         print( dado, end="\t")
#     print()

