'''Calcular qual valor máximo do cashback o usuário pode usar para
abater na nova venda
O cashback utilizado não pode ultrapassar 45% da compra. Faça uma função
em Python que recebe o valor de cashback acumulado pelo cliente e o valor da
venda e retorna o valor do cashback que pode ser utilizado.'''

total_da_compra = 0 ##(Este é o "custo" que Mascariane tem para vender os produtos. Como o valor exato dessa burocracia está em outra questão, vamos deixar zerado por aqui.)

def limite_cash(cashback_em_dinheiro, total_da_venda):
    limite = total_da_venda * 0.45
    if cashback_em_dinheiro > limite:
        cashback_utilizado = total_da_venda * 0.45
        cashback_em_dinheiro = cashback_em_dinheiro - cashback_utilizado
        venda_final_cashback = total_da_venda - cashback_utilizado
        faturamento = (venda_final_cashback - total_da_compra) - 3.5/100
    
