'''(20) Escreva um programa que use uma pilha para verificar se uma expressão matemática
(em String) tem os parênteses agrupados de forma correta, isto é:
a. se o número de parênteses de abertura e fechamento são iguais;
b. se todo parêntese aberto é seguido posteriormente por um fechamento
de parêntese;
c. nenhuma expressão deve conter um parêntese de fechamento antes de
um de abertura.
Ex1: A expressão ((A+B) viola as condições a e b.
Ex2: A expressão A+B) viola as condições a e c.
Ex3: A expressão )A+B( – C viola as condições b e c.
Ex4: A expressão (A+B)) – (C + D violam a condição b e c.'''

pilha = []

abertura = 0
fechamento = 0
indice = 0

expressao = str(input('Digite sua expressão algébrica com parênteses: '))

# for i in expressao:
#     if i == "(":
#         abertura += 1
#     if i == ")":
#         fechamento += 1

# if abertura != fechamento:
#     print(f'Expressão incorreta, verifique seus parênteses {pilha}')

for i in expressao:
    # if indice == 0 and i == ")":
    #     print("Sua expressão está incorrenta.")

    if i == "(":
        pilha.append(i)
        
    elif i == ")":
        if  len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(i)

if len(pilha) == 0:
    print("Expressão correta.")
else:
    print(f'Expressão incorreta, verifique seus parênteses {expressao}')