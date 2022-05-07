'''
Agora vamos incorporar as regras de uso de valor de cashback que o cliente já
conseguiu para abater nessa nova venda.
No momento da finalização da venda, depois que o programa informar a
porcentagem de cashback que o cliente vai obter, o vendedor informa se o cliente vai
querer usar seu saldo de cashback para abater no valor desta nova compra ou se quer
ganhar mais cashback. Se ele escolhe ganhar mais cashback, o programa mostra o total
da compra sem cashback, o total da compra com cashback e, ainda, mostra quanto foi
o faturamento da venda, sabendo que o imposto (pago pela loja) é de 3,5% e
considerando o cashback no cálculo.
Caso ele decida usar o valor do cashback, o vendedor informa ao programa quanto
o cliente tem de cashback e esse valor será descontado do valor final da venda, porém
algumas regras precisam ser aplicadas:
• O cashback só pode ser utilizado se o cliente já tiver acumulado pelo menos
R$25,00. Se for menos que R$25,00, o programa emite uma mensagem e
mostra novamente o valor total a ser pago (além do faturamento).
• O cashback utilizado não pode ultrapassar 45% da compra. Ou seja, se o cliente
tiver acumulado mais que 45% do valor daquela compra, o programa deve abater
apenas os 45% da compra do saldo do cashback, mostrando o valor da compra
com o desconto do cashback (ou seja, 55% do valor original), além de mostrar o
valor de saldo de cashback que ainda restará. Não esqueça do faturamento!
OBS: lembre que o cashback já foi considerado no faturamento na hora que o
cliente o ganhou, agora esse valor é mesmo que dinheiro).
'''

#reaprovetei o código anterior para fazer as modificações solicitadas. Creio que assim fica mais completo.

venda_novo_produto = str(input("Deseja registrar venda de produto? ('yes' or 'no'): ")).lower().strip[0]

total_da_venda = 0
total_da_compra = 0
preco_compra = 0
preco_venda = 0

while venda_novo_produto != "y" and venda_novo_produto != "n":
    venda_novo_produto = str(input("Deseja registrar venda de produto? Digite apenas 'yes' or 'no': ")).lower().strip[0]

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
    
    print(f'O total da venda agora é ${total_da_venda}')
    total_da_venda = total_da_venda + (preco_venda * quant_compra)
    print(f'+ novo produto, o total da venda é ${total_da_venda}')

    total_da_compra = total_da_compra + (preco_compra * quant_compra)
    
    venda_novo_produto = str(input("Deseja registrar uma nova venda de produto? ('yes' or 'no'): ")).lower().strip[0]

    while venda_novo_produto != "y" and venda_novo_produto != "n":
        venda_novo_produto = str(input("Deseja registrar uma nova venda de produto? Digite apenas 'yes' or 'no': ")).lower().strip[0]
        

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

cashback = total_da_venda * cashback
venda_final_cashback = total_da_venda - cashback

faturamento = (venda_final_cashback - total_da_compra) - 3.5/100

print(f'O valor da venda foi de ${total_da_venda:.2f}')
print(f'O cashback é de ${cashback:.2f}')

#o vendedor informa se o cliente vai querer usar seu saldo de cashback para abater no 
# valor desta nova compra ou se quer ganhar mais cashback

uso_cashback = str(input("O cliente deseja usar o cashback ou ganhar mais? Digite 'use' or 'win': ")).lower().strip()

if uso_cashback == "win":
    print(f'O preço final sem cashback é de ${total_da_venda:.2f}')
    print(f"O preço final com o cashback é de ${venda_final_cashback:.2f}")
    print(f"O faturamento é de ${faturamento:.2f}")

if uso_cashback == "use":
    if cashback < 25:
        print("Você ainda não pode usar o cashback!")
        print(f'O preço final é de ${total_da_venda:.2f}')
        print(f'O faturamento, subtraido ao imposto pago e ao cashback, é de ${faturamento:.2f}')

    if cashback > (total_da_venda * 0.45):
        cashback_utilizado = total_da_venda * 0.45
        cashback = cashback - cashback_utilizado
        venda_final_cashback = total_da_venda - cashback_utilizado
        faturamento = (venda_final_cashback - total_da_compra) - 3.5/100

        print(f"O preço final é com o cashback é de ${venda_final_cashback:.2f}")
        print(f'O cashback restante é de {cashback:.2f}')
        print(f"O faturamento é de ${faturamento:.2f}")

    if cashback >= 25:
        print(f'O preço final sem cashback é de ${total_da_venda:.2f}')
        print(f"O preço final é com o cashback é de ${venda_final_cashback:.2f}")
        print(f"O faturamento é de ${faturamento:.2f}")