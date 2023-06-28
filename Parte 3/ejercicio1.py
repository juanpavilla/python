
inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

if inicio <= fin:
    paso = 1
else:
    paso = -1

numeros = list(range(inicio, fin + paso, paso))
print("La lista de números es:", end=" ")
for numero in numeros:
    print(numero, end=", ")
