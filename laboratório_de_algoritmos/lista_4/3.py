'''Mascariane está querendo fazer um cadastro de seus clientes para que esses
dados fiquem salvos e a ajude a tomar algumas decisões como promoções,
envio de e-mails, controle de cashback e etc. Só que ela ainda não sabe
exatamente todas as funcionalidades e informações que vai querer/precisar.
Por enquanto, ela pediu que você criasse uma lista com os nomes dos
clientes em ordem alfabética. Um vendedor vai lhe ajudar nessa missão. Ele vai
informar os nomes dos clientes, um a um, e você vai precisar inserir cada novo
cliente já na posição correta da lista para que a ordem alfabética seja respeitada.
O vendedor sabe quantos clientes tem no total e vai lhe informar logo no início
do programa. Ao final, imprima a listagem de clientes, cada um em uma linha.'''

lista_nomes = []

n = int(input("Número de pessoas: "))

for i in range(n):
    lista_nomes.append(str(input(f"Nome do {i+1}º cliente: ")))

lista_nomes.sort()

for cliente in lista_nomes:
    print(cliente)