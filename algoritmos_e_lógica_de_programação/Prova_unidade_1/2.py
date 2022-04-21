'''O banco NãoDizQuePegouOBesta concederá um crédito especial aos seus
clientes, que dependerá do saldo médio no último ano. Faça um algoritmo que leia o
saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela abaixo.
Mostre uma mensagem informando o saldo médio e o valor do crédito.'''

saldo_medio = int(input("Informe o saldo médio do cliente: $"))

if saldo_medio < 200:
    print(f'Saldo médio: {saldo_medio}')
    print("Nenhum crédito")
elif saldo_medio >=201 and saldo_medio <= 400:
    credito = saldo_medio *0.2
    print(f'Saldo médio: {saldo_medio}')
    print(f'Crédito de até ${credito}')
elif saldo_medio >= 401 and saldo_medio <= 600:
    credito = saldo_medio * 0.3
    print(f'Saldo médio: {saldo_medio}')
    print(f'Crédito de até ${credito}')
elif saldo_medio >= 601:
    credito = saldo_medio * 0.4
    print(f'Saldo médio: {saldo_medio}')
    print(f'Crédito de até ${credito}')
else:
    print("Algo está errado, tente novamente.")
