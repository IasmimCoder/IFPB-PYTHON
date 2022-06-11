'''Implemente uma função recursiva que receba uma string e diga quantas
letras ele tem. Crie um programa que use essa função.'''

### FUNÇÕES ###

def letrasRec(frase):
    frase =  "".join(frase.strip().split())
    if frase == "":
        return 0
    else:
        return 1 + letrasRec(frase[1:])

### INÍCIO ###

frase_input = str(input("Digite uma string qualquer: "))
qtd_letras = letrasRec(frase_input)
print(f"Essa string contém {qtd_letras} caracteres.")