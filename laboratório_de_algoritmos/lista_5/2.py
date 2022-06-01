"""Agora você vai fazer o cadastro de produtos vendidos pela PassaAlcool70
em uma matriz. Cada linha da matriz representará um produto; cada coluna, uma
informação do produto.
Você vai fazer um programa em Python que permita que o vendedor
preencha esse cadastro. O vendedor inicialmente informará o número de
produtos a serem cadastrados. Para cada produto, o programa irá solicitar ao
vendedor:
• Código com 6 dígitos – fazer validação de quantidade de dígitos
• Descrição do produto
• Estoque mínimo – validação de precisar ser maior que 0
• Preço de compra
• Preço de venda
Ao fim, o programa deve imprimir o cadastro de produtos, um produto por linha."""

matriz = []
informacoes = ['código de 6 dígitos', 'descrição do produto', 'estoque mínimo', 'preço de compra', 'preço de venda']
index_produto = 0
qtd_produtos = int(input("Quantos produtos serão cadastrados? "))

for i in range(qtd_produtos):
    linha_produto = []

    index_produto += 1

    print("---"*5)
    print(f"{index_produto}º PRODUTO NOVO")
    print("---"*5)

    for x in range(5):
        print(f"Informe o {informacoes[x]}:")
        informacao = input()
        
        while x == 0 and len(informacao) != 6:
            print(f"Informe o {informacoes[x]}:")
            informacao = input()

        while x == 2 and int(informacao) < 1:
            print(f"Informe o {informacoes[x]}:")
            informacao = input()
    
        linha_produto.append(informacao)
       
        
    matriz.append(linha_produto)
    
for produto in matriz:
    print(produto)
