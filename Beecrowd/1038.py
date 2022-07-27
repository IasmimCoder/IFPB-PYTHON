code, qtd = input().split(" ")
code = int(code)
qtd = int(qtd)

#validação a fazer p/ melhorar 
precos = [4, 4.5, 5, 2, 1.5]

preco_item = precos.pop(code -1)

total = preco_item * qtd

print(f"Total: R$ {total:.2f}")


# if code == 1:
#     preco = 4
# elif code == 2:
#     preco = 4.5
# elif code == 3:
#     preco = 5
# elif code == 4:
#     preco = 2
# elif code == 5:
#     preco = 1.5