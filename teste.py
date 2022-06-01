def cashback_function(num_compras = 0):
    if num_compras == 5:
        cashback = 0.01
    elif num_compras > 5 and num_compras <= 10:
        cashback = 0.015
    elif num_compras > 10:
        cashback = 0.02
    else:
        print("Não receberá cashback: número de compras insuficiente.")
    print(cashback)

num_compras = int(input())

cashback_function(num_compras)