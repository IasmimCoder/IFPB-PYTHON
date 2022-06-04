'''Faça um programa em Python que converta da notação de 24 horas para a notação
de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada
é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para a saída. Assim, a função para efetuar as conversões terá um
parâmetro para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário
repita esse cálculo para novos valores de entrada todas as vezes que desejar.'''

#### VARIÁVEIS E FUNÇÕES

def conversaoHoras(horas):
    if horas > 12:
        return "P.M"
    else:
        return "A.M"


def mostrarHoras(horas, minutos, parametro):
    if parametro == "P.M":
        horas = horas - 12

    return(f"{horas}:{minutos} {parametro}")

###### INÍCIO #######

hrs_input = int(input("Digite as horas: "))

while hrs_input < 0 or hrs_input >= 24:
    hrs_input = int(input("Digite as horas novamente: "))

min_input = int(input("Digite os minutos: "))

while min_input < 0 or min_input >= 60:
    min_input = int(input("Digite os minutos novamente: "))

parametro = conversaoHoras(hrs_input)
print(mostrarHoras(hrs_input, min_input, parametro))
