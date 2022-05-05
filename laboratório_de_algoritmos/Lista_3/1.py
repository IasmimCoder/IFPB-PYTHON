'''
1. Estoque
Dentre todos os produtos que a PassaAlcool70 vende, os campeões são os
presentes na tabela abaixo. Esses produtos não podem faltar de jeito nenhum e, por
isso, Mascariane quer controlar o estoque. O número mínimo de unidades de cada um
desses produtos também está na tabela. Mascariane quer que quando o estoquista
informe o código de um produto e a quantidade de unidades dele no estoque, o
programa retorne se já é hora de fazer o pedido ou não, dado que o pedido deve ser
feito quando o estoque tiver entre 15% e 20% acima do mínimo de unidades para que
o estoque não fique desabastecido. 

O programa deve permitir que o estoquista realize
várias consultas em sequência e avise quando não mais quiser consultar o estoque. O
estoquista fará a consulta com frequência, então não precisa se preocupar com a
situação de uma consulta quando o estoque tiver abaixo de 15%.

'''
consulta = str(input("Deseja realizar uma consulta no estoque? ('yes' or 'no'): ")).lower()

while consulta != "yes" and consulta != "no": 
    consulta = str(input("Deseja realizar uma consulta? Digite apenas 'yes' or 'no': ")).lower()

while consulta == "yes": 

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
    elif cod_produto == "04": 
        nome = "Máscara N95"
        est_min = 200
    elif cod_produto == "05":
        nome = "Cx. Másc. tripla camada"
        est_min = 50

    alerta_leve = est_min + (est_min * 0.20)
    alerta_grave = est_min+ (est_min * 0.15)
    porcentagem_estoque = ((estoque_atual * 100)/est_min)-100


    if estoque_atual > alerta_leve:
        print(f'Nova estocagem não é necessária.')
    elif (estoque_atual <= alerta_leve and estoque_atual >= alerta_grave) :
        print(f'Atenção! Já é hora de fazer o pedido.')
    elif (estoque_atual < alerta_grave):
        print(f'Urgente!')
    else:
        print("Algo está errado.")

    print(f'Seu estoque atual está {porcentagem_estoque:.1f}% acima do estoque mínimo desse produto.')

    consulta = str(input("Deseja realizar mais uma consulta? ('yes' or 'no'): ")).lower()

    while consulta != "yes" and consulta != "no": 
        consulta = str(input("Deseja realizar mais uma consulta? Digite apenas 'yes' or 'no': ")).lower()
    if consulta == "no":
        print("Bom trabalho!")
    
