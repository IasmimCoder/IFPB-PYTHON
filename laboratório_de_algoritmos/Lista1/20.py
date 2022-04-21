valor_refeicao = float(input("Digite o valor da refeição: "))
gorjeta = valor_refeicao * 0.10
impostos = valor_refeicao * 0.07
total = valor_refeicao + gorjeta + impostos 

print(f'Valor da refeição: ${valor_refeicao}.')
print(f'10% para gorjeta: ${gorjeta}')
print(f'7% para impostos: ${impostos}')
print(f'-----_TOTAL------: ${total}')
