def verificar_numero():
    numero = input("Ingrese un número: ")

    if "." in numero:
        print("El número", numero, "es un número real.")
    elif numero.isdigit():
        print("El número", numero, "es un número entero.")
    else:
        print("El valor ingresado no es un número válido.")

verificar_numero()
