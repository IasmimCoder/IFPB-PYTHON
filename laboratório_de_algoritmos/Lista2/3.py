'''
Mascariane é muito antenada e, para fidelizar os clientes quer implementar um
cashback de acordo com o número de compras já realizadas pelo cliente. Clientes que
compraram pelo menos 5 vezes tem 1% de cashback. Clientes que compraram entre 5
e 10 vezes tem 1,5% de cashback. Clientes que compraram mais de 10 vezes tem 2%
de cashback. O vendedor informa o número de compras do cliente e o total da venda e
seu programa deve mostrar o valor do cashback que o cliente receberá.
'''

num_compras = int(input("Informe o número de compras do cliente: "))
total_da_venda = float(input("Informe o total da venda: "))

if num_compras >= 5:
    cashback = total_da_venda * 0.01
elif num_compras > 5 and num_compras <= 10:
    cashback = total_da_venda * 0.015
elif num_compras > 10:
    cashback = total_da_venda * 0.02
else:
    print("Não receberá cashback: número de compras insuficiente.")

print(f'O cashback é de {cashback}')
