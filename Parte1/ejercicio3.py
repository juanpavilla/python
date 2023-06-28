binario = input("Ingrese un número binario: ")

decimal = 0
exp = len(binario) - 1

for digito in binario:
    decimal += int(digito) * (2 ** exp)
    exp -= 1

print("El número decimal equivalente a binario es :", decimal)
