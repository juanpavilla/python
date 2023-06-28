n = int(input("Ingrese un número: "))
if n == 0:
    factorial = 1
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
print("El factorial de", n, "es:", factorial)
