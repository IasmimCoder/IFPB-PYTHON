'''
Mascariane quer que quando o estoquista informe o
código de um produto e a quantidade de unidades dele no estoque, o programa retorne
se já é hora de fazer o pedido ou não, dado que o pedido deve ser feito quando o
estoque tiver entre 15% e 20% acima do mínimo de unidades para que o estoque não
fique desabastecido. O estoquista fará a consulta com frequência, então não precisa se
preocupar com a situação de uma consulta quando o estoque tiver abaixo de 15%.
'''
cod_produto = str(input("Informe o código do produto: "))
estoque_atual = int(input("Informe o estoque desse produto: "))


if cod_produto == "01":
    nome = "Álcool 70% em Gel"
    est_min = 500
elif cod_produto == "02":
    nome = "Álcool 70% Líquido"
    est_min = 780
elif cod_produto == "03":
    nome = "Solução Sanitizante"
    est_min = 340

alerta_leve = est_min + (est_min * 0.20)
alerta_grave = est_min+ (est_min * 0.15)
porcentagem_estoque = ((estoque_atual * 100)/est_min)-100

'''
print(f"Código\t|Produto\t\t|Estoque mínimo\t| Preço de compra p/ unidade | preço de venda p/ unidade")
print(f"{cod_produto}|\t{nome}\t\t|{est_min}\t|")
'''

if estoque_atual > alerta_leve:
    print(f'Nova estocagem não é necessária.')
elif (estoque_atual <= alerta_leve and estoque_atual >= alerta_grave) :
    print(f'Atenção! Já é hora de fazer o pedido.')
elif (estoque_atual < alerta_grave):
    print(f'Urgente!')
else:
    print("Algo está errado.")

print(f'Seu estoque atual está {porcentagem_estoque:.1f}% acima do estoque mínimo desse produto.')
