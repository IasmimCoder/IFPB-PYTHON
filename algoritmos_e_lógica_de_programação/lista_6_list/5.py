'''Existem partes de sistemas operacionais que cuidam da ordem em que os
programas devem ser executados. Existe a necessidade de manter um conjunto de
processos em uma fila, esperando para serem executados. Escreva um programa
em Python que seja capaz de ler dois comandos (adicionar, remover). Caso a
pessoa digite "adicionar", ela deve dizer o nome do processo para ser adicionado
na fila, e a fila deve ser impressa. Caso a pessoa digite "remover", o processo
removido deve aparecer na tela, e a fila deve ser impressa. O programa para caso
a pessoa digite "fim". Caso a pessoa digite algo que não seja "adicionar" ou
"remover" ou “fim”, avisar que o comando está inválido. Se tentar remover algo da
fila vazia, avisar que a fila está vazia.'''

fila = []

comando = str(input("Digite 'adicionar' ou 'remover': ")).lower().split()

while comando != "adicionar" and comando != "remover" and comando != "fim":
    comando = str(input("Comando inválido. Digite apenas 'adicionar' ou 'remover': ")).lower().split()

if comando == "adicionar":
    fila.append(str(input("Informe o novo processo: ")))
    print(fila)

if comando == "remover":
    if len(fila) == 0:
        print("A fila está vazia")
    else:
        removido = fila.pop(0)
        print(removido)
        print(fila)

print("Programa finalizado.")