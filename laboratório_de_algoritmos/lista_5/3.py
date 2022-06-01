'''3. Calcular porcentagem de cashback
Lembra que na PassaAlcool o cliente tem direito a cashback? Quando o
cliente atinge 5 compras, tem direito a 1% de cashback. Clientes que compraram
de 6 a 10 vezes tem 1,5% de cashback. Clientes que compraram mais de 10
vezes tem 2% de cashback. Faça uma função em Python que calcula a
porcentagem de cashback que o cliente terá direito, Para isso, a função receberá
o número de compras como parâmetro e retornará a porcentagem.
Modifique a sua solução da questão 2 do laboratório 3 para que ela utilize
esta função.'''

def cashback_function(num_compras = 0):

    if num_compras == 5:
        cashback = 0.01
    elif num_compras > 5 and num_compras <= 10:
        cashback = 0.015
    elif num_compras > 10:
        cashback = 0.02
    elif num_compras < 5:
        print("Não receberá cashback: número de compras insuficiente.")
  

    print(f"O cashback é de {cashback*100}%.")

# cashback_function()


