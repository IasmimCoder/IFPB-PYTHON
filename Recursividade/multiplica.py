def multiplica(num1, num2):

    #multiplicação por 0 é 0
    if num1 == 0 or num2 == 0:
        return 0

    #Caso base, onde a recursão para
    elif num2 == 1:
        return num1
    
    #Multiplicação através da soma com recursividade
    else:
        return (num1 + (multiplica(num1, num2 - 1)))

number1 = int(input("Nº 1: "))
number2 = int(input("Nº 2: "))

produto = multiplica(number1, number2)
print(f"O produto entre {number1} e {number2} é {produto}.")