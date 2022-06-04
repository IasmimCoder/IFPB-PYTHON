'''Escreva uma função em Python que recebe uma String e retorna um Boolean
dizendo se é um palíndromo ou não. Faça um programa que use essa função.'''

def palíndromo(string):
    stringInvertida = string[::-1]

    if stringInvertida == string:
        return True
    else:
        return False

        
# string sem espacos -> replace(' ', '')
#string minuscula -> lower()

x = str(input("Digite uma frase ou número: "))
string = x.replace(' ', '').lower()
trueOrFalse = palíndromo(string)
print(f"{x} é um palíndromo: {trueOrFalse}")

