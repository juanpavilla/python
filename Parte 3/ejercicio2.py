
inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))
if inicio % 2 != 0:
    inicio += 1

print("Los números pares desde", inicio, "hasta", fin, "son:")
for numero in range(inicio, fin + 1, 2):
    print(numero)
