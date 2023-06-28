def encontrar_mayor():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if numero1 > numero2:
        print("El número", numero1, "es el mayor.")
    elif numero2 > numero1:
        print("El número", numero2, "es el mayor.")
    else:
        print("Los números son iguales.")

encontrar_mayor()
