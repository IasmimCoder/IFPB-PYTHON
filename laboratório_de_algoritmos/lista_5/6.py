'''Agora, modifique a sua solução da questão 3 do laboratório 3 para que ela
utilize as funções das questões 4 e 5.'''
    
def cashback_function(num_compras = 0):
    if num_compras == 5:
        cashback = 0.01
    elif num_compras > 5 and num_compras <= 10:
        cashback = 0.015
    elif num_compras > 10:
        cashback = 0.02
    else:
        print("Não receberá cashback: número de compras insuficiente.")
    return cashback
    
def valor_minimo_cashback(cashback):

    if cashback >= 25:
        return(True)
       
    else:
        return(False)
        

def limite_cash(cashback_em_dinheiro, valor_venda):
    limite = valor_venda * 0.45
    if cashback_em_dinheiro > limite:
        cashback_utilizado = total_da_venda * 0.45
        cashback_em_dinheiro = cashback_em_dinheiro - cashback_utilizado
        venda_final_cashback = total_da_venda - cashback_utilizado
        faturamento = (venda_final_cashback - total_da_compra) - 3.5/100


###registro e seleção de produtos. 
venda_novo_produto = str(input("Deseja registrar venda de produto? ('yes' or 'no'): ")).lower().strip()[0]

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
    
    venda_novo_produto = str(input("Deseja registrar uma nova venda de produto? ('yes' or 'no'): ")).lower().strip()[0]

    while venda_novo_produto != "y" and venda_novo_produto != "n":
        venda_novo_produto = str(input("Deseja registrar uma nova venda de produto? Digite apenas 'yes' or 'no': ")).lower().strip()[0]
        

print(f"Ok! O total parcial da venda é de ${total_da_venda}")

#definição cashback
num_compras = int(input("Informe o número de compras já realizadas do cliente: "))
cashback_retorno = cashback_function(num_compras)

cashback_em_dinheiro = total_da_venda * cashback_retorno
venda_final_cashback = total_da_venda - cashback_em_dinheiro
faturamento = (venda_final_cashback - total_da_compra) - 3.5/100

print(f'O valor da venda foi de ${total_da_venda:.2f}')
print(f'O cashback é de ${cashback_em_dinheiro:.2f}')


#o vendedor informa se o cliente vai querer usar seu saldo de cashback para abater no 
# valor desta nova compra ou se quer ganhar mais cashback


uso_cashback = str(input("O cliente deseja usar o cashback ou ganhar mais? Digite 'use' or 'win': ")).lower().strip()

if uso_cashback == "win":
    print(f'O preço final sem cashback é de ${total_da_venda:.2f}')
    print(f"O preço final com o cashback é de ${venda_final_cashback:.2f}")
    print(f"O faturamento é de ${faturamento:.2f}")

if uso_cashback == "use":

    if valor_minimo_cashback(cashback_em_dinheiro) == True:
        if valor_minimo_cashback == True:
            limite_cash(cashback_em_dinheiro, total_da_venda)
        print(f'O preço final sem cashback é de ${total_da_venda:.2f}')
        print(f"O preço final é com o cashback é de ${venda_final_cashback:.2f}")
        print(f'O cashback acumulado restante é de {cashback_em_dinheiro:.2f}')
        print(f"O faturamento é de ${faturamento:.2f}")
    else:
        print("Você ainda não pode usar o cashback!")
        print(f'O preço final é de ${total_da_venda:.2f}')
        faturamento = total_da_compra - 3.5/100
        print(f'O faturamento, subtraido ao imposto pago é de ${faturamento:.2f}')
    
   


