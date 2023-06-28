def verificar_edad():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    if edad < 18:
        print(nombre, "Usted es menor de edad.")
        print("Prohibido el ingreso. Apenas tienes", edad, "Años")
    else:
        documento = input("Ingrese su número de documento: ")
        print("¡Bienvenido,", nombre + "!")
        print("Puede ingresar.")

verificar_edad()
