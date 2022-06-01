'''4. Determinar se o cliente já pode utilizar o cashback
O cashback só pode ser utilizado se o cliente já tiver acumulado pelo menos
R$25,00. Faça uma função em Python que recebe o valor de cashback
acumulado pelo cliente e retorna um boolean, determinado se o cashback já
pode ser utilizado.'''

def valor_acumulado(x):
    
    if x >= 25:
        print(True)
    else:
        print(False)
    
# valor_acumulado()
