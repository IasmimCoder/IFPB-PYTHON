'''Escreva uma função recursiva que recebe uma string e conta quantos “A”
aparece nele. Crie o programa que chame a função e mostre a resposta.'''

### FUNÇÕES ###

def conteA(x):
    if x == "":
        return 0
    else:
        elemento = x[0]
        if elemento == "a" or elemento == "A":
            return 1 + conteA(x[1:])
        else:
            return conteA(x[1:])

### INÍCIO ###

frase = str(input("Digite uma frase: "))
qtd_a = conteA(frase)
print(f"Esta frase contém {qtd_a} letras 'a'.")
