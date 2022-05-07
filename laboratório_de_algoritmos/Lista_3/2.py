'''
2. Venda com cashback
Mascariane é muito antenada e, para fidelizar os clientes quer implementar um
cashback de acordo com o número de compras já realizadas pelo cliente. Quando o
cliente atinge 5 compras, tem direito a 1% de cashback. Clientes que compraram de 6
a 10 vezes tem 1,5% de cashback. Clientes que compraram mais de 10 vezes tem 2%
de cashback.

Para o controle de venda, que agora vai permitir mais de um produto por cliente por
vez, o vendedor deve informar o código do produto e a quantidade que o cliente vai
comprar e o programa deve retornar o valor parcial da venda. O programa deve
perguntar ao vendedor se ele vai registrar a venda de outro produto até que ele decida
não mais informar. Em caso afirmativo, vai repetir o processo anterior, atualizando o
valor parcial da venda. Em caso negativo, o programa vai proceder a finalização da
venda.

Para finalizar a venda, o vendedor informa número de compras já realizadas pelo
cliente e o programa informa a porcentagem de cashback, o total da compra sem
cashback, o total da compra com cashback e, ainda, mostra quanto foi o faturamento da
venda, sabendo que o imposto (pago pela loja) é de 3,5% e considerando o cashback
no cálculo.
'''
total_da_venda = 0
total_da_compra = 0
preco_compra = 0
preco_venda = 0

venda_novo_produto = str(input("Deseja registrar venda de produto? ('yes' or 'no'): ")).lower().strip()[0]

while venda_novo_produto != "y" and venda_novo_produto != "n":
    venda_novo_produto = str(input("Deseja registrar venda de produto? Digite apenas 'yes' or 'no': ")).lower().strip()[0]

while venda_novo_produto == "y":

    cod_produto = str(input("Informe o código do produto: "))
    quant_compra = int(input("Informe a quantidade que o cliente vai comprar: "))


    if cod_produto == "01":
        preco_venda = 18
        preco_compra = 12.5
    elif cod_produto == "02":
        preco_venda = 9.5
        preco_compra = 5
    elif cod_produto == "03":
        preco_venda = 27
        preco_compra = 22
    elif cod_produto == "04":
        preco_venda = 5
        preco_compra = 3.5
    elif cod_produto == "04":
        preco_venda = 15
        preco_compra = 9.9
    
    print(f'O total da venda era ${total_da_venda}')
    total_da_venda = total_da_venda + (preco_venda * quant_compra)
    print(f'+ novo produto, o total da venda agora é ${total_da_venda}')
    total_da_compra = total_da_compra + (preco_compra * quant_compra)
    
    venda_novo_produto = str(input("Deseja registrar uma nova venda de produto? ('yes' or 'no'): ")).lower().strip()[0]

    while venda_novo_produto != "y" and venda_novo_produto != "n":
        venda_novo_produto = str(input("Deseja registrar uma nova venda de produto? Digite apenas 'yes' or 'no': ")).lower().strip()[0]
        

print(f"Ok! O total parcial da venda é de ${total_da_venda}")


num_compras = int(input("Informe o número de compras já realizadas do cliente: "))

cashback = 0 

if num_compras >= 5:
    cashback = 0.01
elif num_compras > 5 and num_compras <= 10:
    cashback = 0.015
elif num_compras > 10:
    cashback = 0.02
else:
    print("Não receberá cashback: número de compras insuficiente.")

venda_final = total_da_venda - (total_da_venda * cashback)

faturamento = (venda_final - total_da_compra) - 3.5/100

print(f'O valor da venda foi de ${total_da_venda:.2f}')
print(f'O cashback é de {cashback*100}%')
print(f"O preço final é ${venda_final}")
print(f'O faturamento, subtraido ao imposto pago e ao cashback, é de ${faturamento:.2f}')
