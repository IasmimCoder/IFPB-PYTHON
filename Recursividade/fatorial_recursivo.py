def fatorial(num):
    if num <= 1:
        return 1
    
    return num * fatorial(num - 1) 

num = int(input())
resultado = fatorial(num)
print(resultado)
