'''Você quer retirar seus livros da estante e colocá-los um em cima do outro para limpá-
los. Depois disso, você quer separar o livro que você mais gosta. Para isso, você
precisa desempilhar esses livros colocando-os em uma pilha ao lado, até achar seu
favorito, após isso, precisa reempilhar os livros na pilha original. Crie um programa
e, Python que receba 20 nomes de livros vindos da estante. Empilhe-os. Depois
receba o nome do seu livro favorito (tem que estar entre os que foram retirados da
estante) e execute o procedimento descrito acima para achá-lo na pilha original e
retirá-lo de lá. Reempilhe os livros na pilha original.'''

### empilhando
pilha_temporaria = []
pilha_original = []
for i in range(20):
    pilha_original.append(str(input(f"Digite o nome do {i+1}º livro: ")))

### receber nome do livro favorito
livro_favorito = "arte da guerra"

### achar o livro_favorito na pilha_original 

livro_pego = ''
while livro_pego != livro_favorito:
    livro_pego = pilha_original.pop()
    if livro_pego != livro_favorito:
        pilha_temporaria.append(livro_pego)

print(f'pilha temporária: {pilha_temporaria}')
print(f'pilha original: {pilha_original}')
print(f'livro pego: {livro_pego}')
print("==="*10)

for i in range(len(pilha_temporaria)):
    livro = pilha_temporaria.pop()
    pilha_original.append(livro)
    
print(f'pilha temporária: {pilha_temporaria}')
print(f'pilha original: {pilha_original}')
print(f'livro pego: {livro_pego}')
