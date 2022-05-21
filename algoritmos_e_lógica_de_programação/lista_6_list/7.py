"""Escreva um programa que receba uma linha de texto e use uma pilha para exibir a
linha invertida."""


texto = "Ola mundo do Python"
pilha_invertido = []
texto_invertido = ''
for i in range(len(texto)-1, 1, -1):
    pilha_invertido.append(texto[i])

texto_invertido = ''.join(pilha_invertido)
print(texto_invertido)