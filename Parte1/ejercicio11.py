def obtener_longitud():
    dato = input("Ingrese un dato: ")

    contador = 0
    for caracter in dato:
        contador += 1

    print("La longitud del dato es:", contador)

obtener_longitud()
