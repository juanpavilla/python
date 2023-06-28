numero = float(input("Ingrese un número: "))

if numero >= 0:
    raiz_cuadrada = numero ** 0.5
    print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
else:
    raiz_cuadrada = (-numero) ** 0.5
    print("La raíz cuadrada de", numero, "es:", raiz_cuadrada, "negativo")
