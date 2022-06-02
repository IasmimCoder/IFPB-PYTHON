def fibonacci(ordem):
    if ordem == 1:
        return 0
    elif ordem == 2:
        return 1
    
    return fibonacci(ordem -1) + fibonacci(ordem - 2)

ordem = int(input())
print(f"Fibonacci: {fibonacci(ordem)}")