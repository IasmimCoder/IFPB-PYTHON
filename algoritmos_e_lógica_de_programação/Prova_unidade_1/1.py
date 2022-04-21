'''(20) Fumizeldo quer calcular e mostrar a quantidade de litros de combustível gastos
em uma viagem, ao utilizar um automóvel que faz 12 km/l. Para isso, ele gostaria
que você o auxiliasse através de um simples programa em Python. Para efetuar o
cálculo, o programa deve pedir ao usuário o tempo gasto na viagem (em horas) e a
velocidade média durante a mesma (em km/h). Assim, pode-se obter distância
percorrida e, em seguida, calcular quantos litros seriam necessários. O programa
deve imprimir o tempo gasto na viagem, a velocidade média, a distância percorrida
e a quantidade de litros necessários.'''

tempo_viagem = float(input("Quantas horas você gastou na viagem? "))
velocidade = float(input("Qual a velocidade? (KM/H) "))

distancia = velocidade*tempo_viagem
litros = distancia/12


print(f'O tempo gasto na viagem foi de {tempo_viagem}, com a velocidade média de {velocidade}, na distância de {distancia} KM.')
print(f'A quantidade de litros necessários é de {litros}.')
