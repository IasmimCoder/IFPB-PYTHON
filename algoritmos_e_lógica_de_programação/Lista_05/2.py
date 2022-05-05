'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
'''

user = str(input("Digite o seu nome de usuario: ")).lower()
keyword = str(input("Digite sua senha: ")).lower()

while user == keyword: 
    print("Erro. Sua senha não pode ser idêntica ao seu nome de usuário! Digite novamente suas informações: ")
    user = str(input("Digite o seu nome de usuario: ")).lower()
    keyword = str(input("Digite sua senha: ")).lower()

if user != keyword:
    print("Ok!")
    
