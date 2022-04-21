nome= (input("Informe seu nome: "))
matricula= (input("Informe sua matrícula: "))
print("Bem vindo ao sistema,", nome, "! Boas vendas.")

produto1 = float(input("Digite o valor do primeiro produto: "))
quant1 = int(input("Unidades: "))

produto2 = float(input("Digite o valor do segundo produto: "))
quant2 = int(input("Unidades: "))

produto3 = float(input("Digite o valor do terceiro produto: "))
quant3 = int(input("Unidades: "))

total = float(produto1 * quant1 + produto2 * quant2+ produto3 * quant3)
comissao = (total * 12)/100
print("O total da compra foi de",total,".")
print("Vendedor: ", nome, "Matrícula: ", matricula, "Comissão: ", comissao )
