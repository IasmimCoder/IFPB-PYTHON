#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a
#letra, escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = str(input("Digite o seu sexo (F/M):"))

if (letra == "F") or (letra == "f"):
    print("F - Feminino")
elif (letra == "M") or (letra == "m"):
    print("M - Masculino")
else: 
    print("Sexo inválido.")