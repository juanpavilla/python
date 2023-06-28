def verificar_par_impar():
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    print("El número", numero, "es", resultado + ".")

verificar_par_impar()
