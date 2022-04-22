'''O IFPB-Monteiro precisa saber, por setor, se o funcionário tomou vacina contra
Covid-19 e qual vacina tomou. Escreva um programa em Python que pergunte ao
usuário o número de funcionários no setor. Depois, para cada um desses
funcionários, o usuário deve informar o nome e se ele já tomou vacina (pelo menos
uma dose ou dose única). Caso o funcionário já tenha tomado, ele deve informar
qual vacina foi tomada (use os seguintes códigos: ‘Astrazeneca’, ’Coronavac’,
‘Jansen’ e ’Pfizer’). O programa deve imprimir as informações de cada funcionário.
Ao final, o programa deve imprimir o número de funcionários do setor, o número de
funcionários que não tomou vacina ainda e o número de funcionários que tomou
cada uma das vacinas elencadas.'''

nao_vacinados = 0
vac_ast = 0
vac_corona =0
vac_jansen = 0
vac_pfizer = 0

num_funcionarios = int(input("Digite o número de funcionários no setor: "))

for x in range(1, num_funcionarios+1):
    nome = str(input(f"Nome do(a) {x}º funcionário(a): "))
    vacina = str(input("Este tomou a 1º dose da vacina? ('yes/y' or 'no/n'): ")).strip().lower()[0]
    print(vacina)
    if vacina == "y":
        tipo_vacina = str(input("Qual vacina este funcionário(a) tomou? (‘Astrazeneca’, ’Coronavac’, ‘Jansen’ e ’Pfizer’): ")).strip().lower()
        if tipo_vacina == "astrazeneca":
                vac_ast += 1
        elif tipo_vacina == "coronavac":
                vac_corona += 1
        elif tipo_vacina == "jansen":
                vac_jansen += 1
        elif tipo_vacina == "pfizer":
                vac_pfizer += 1
        print(f"O/A funcionário(a) {nome} tomou a vacina {tipo_vacina.title()}.")
    elif vacina == "n":
        nao_vacinados += 1
        print(f"O/A funcionário(a) {nome} não tomou a vacina contra Covid-19")



print(f"O setor tem {num_funcionarios} funcionários. {nao_vacinados} não foram vacinados.")
print(f"Os vacinados são: {vac_ast} Astrazeneca, {vac_corona} Coronavac, {vac_jansen} Jansen e {vac_pfizer} Pfizer.")

    
