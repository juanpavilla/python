continuar = True
numero = int(input("Ingrese un número: "))

while continuar:
    print(numero)
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 's':
        numero += 1
    else:
        continuar = False
