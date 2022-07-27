def elevar(k, n):
    if n == 0:
      return 1
    else:
        return k * elevar(k, n-1)
        
        
number = 5
expoente = 5

total = elevar(number, expoente)
print(total)