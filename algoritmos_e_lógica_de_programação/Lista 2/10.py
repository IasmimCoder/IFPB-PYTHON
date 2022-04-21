x = int(input("Digite um valor inteiro para x: "))
y = int(input("Digite outro valor inteiro para y: "))
z = int(input("Digite um valor inteiro para z: "))

w = x * y < z / x or x / y > z * x and z * y < x

print(f'O valor de w é {w}')
