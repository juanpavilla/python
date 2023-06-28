contrasena_inventada = "juanpablo123"

while True:
    contrasena = input("Ingrese la contraseña: ")
    if contrasena == contrasena_inventada:
        print("Contraseña correcta. Puede continuar.")
        break
    else:
        print("Contraseña incorrecta. Inténtelo nuevamente.")

print("Programa continuado...")
