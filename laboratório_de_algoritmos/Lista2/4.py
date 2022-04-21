'''
Para agilizar o trabalho do vendedor, faça um programa que reúna as soluções Venda
e Cashback. Ou seja, na venda, o vendedor já informa o número de compras já
realizadas pelo cliente e o programa já informa o cashback. Porém, agora você também
deve considerar o valor do cashback no cálculo do faturamento.
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

total_da_venda = preco_venda * quant_compra
total_da_compra = preco_compra * quant_compra

num_compras = int(input("Informe o número de compras do cliente: "))

if num_compras >= 5:
    cashback = total_da_venda * 0.01
elif num_compras > 5 and num_compras <= 10:
    cashback = total_da_venda * 0.015
elif num_compras > 10:
    cashback = total_da_venda * 0.02
else:
    print("Não receberá cashback: número de compras insuficiente.")


faturamento = ((total_da_venda - total_da_compra) - 3.5/100) - cashback

print(f'O valor da venda foi de ${total_da_venda:.1f}')
print(f'O cashback é de ${cashback}')
print(f'O faturamento, subtraido ao imposto pago e ao cashback, é de ${faturamento:.1f}')
