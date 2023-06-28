def determinar_tipo_dato():
    dato = input("Ingrese un dato: ")

    if dato.isdigit():
        tipo_dato = "Entero"
    elif dato.replace('.', '', 1).isdigit():
        tipo_dato = "Flotante"
    elif dato.lower() == 'true' or dato.lower() == 'false':
        tipo_dato = "Booleano"
    else:
        tipo_dato = "Cadena de texto"

    print("El tipo de dato ingresado es:", tipo_dato)

determinar_tipo_dato()
