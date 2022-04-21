'''
Para o controle de venda, o vendedor deve informar o código do produto e a quantidade
que o cliente vai comprar e o programa deve retornar o valor da venda e quanto foi o
faturamento da venda, sabendo que o imposto é de 3,5%.
'''
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

valor_venda = preco_venda * quant_compra
valor_compra = preco_compra * quant_compra


faturamento = (valor_venda - valor_compra) - 3.5/100

print(f'O valor da venda foi de {valor_venda:.1f}')
print(f'O faturamento, subtraido ao imposto pago, é de {faturamento:.1f}')
