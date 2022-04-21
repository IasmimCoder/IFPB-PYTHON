#Faça um programa que verifique se uma letra digitada é vogal ou consoante.

alfa = input("Informe uma vogal ou consoante:")

if alfa.isalpha():
    if alfa =="a":
        print("Vogal")
    elif alfa == "e":
        print("Vogal")
    elif alfa == "i":
        print("Vogal")
    elif alfa == "o":
        print("Vogal")
    elif alfa == "u":
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Não é uma letra!")