def factorial(num, forma):
   fact = 1
    if forma == 0:
        i = 1
        while i < num:
            fact = fact * i
            i = i + 1
        fact = fact * num
    if forma == 1:
        fact = math.factorial(num)
    return fact
    break

print("El factorial de 4 es", factorial(4,0))
