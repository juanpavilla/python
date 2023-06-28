contrasena_inventada = "juanpablo123"
intentos = 3

while intentos > 0:
    contrasena = input("Ingrese la contraseña: ")
    if contrasena == contrasena_inventada:
        print("Contraseña correcta. Puede continuar.")
        break
    else:
        intentos -= 1
        print("Contraseña incorrecta. Le quedan", intentos, "intentos.")

if intentos == 0:
    print("Ha agotado todos los intentos. No puede continuar.")
