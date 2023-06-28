def calcular_costo_total():
    costo_campanario = int(input("Ingrese el costo del café en Campanario: "))
    costo_terraplaza = int(input("Ingrese el costo del café en Terraplaza: "))
    costo_transporte = int(input("Ingrese el costo del transporte: "))

    costo_total_campanario = (costo_campanario * 2) + (costo_transporte * 2)
    costo_total_terraplaza = (costo_terraplaza * 2)

    if costo_total_campanario < costo_total_terraplaza:
        print("La mejor opción para Tatiana es ir al Centro Comercial Campanario.")
        print("El costo total sería:", costo_total_campanario)
    elif costo_total_terraplaza < costo_total_campanario:
        print("La mejor opción para Tatiana es ir a Terraplaza.")
        print("El costo total sería:", costo_total_terraplaza)
    else:
        print("Ambas opciones tienen el mismo costo total.")
        print("Puedes elegir entre ir al Centro Comercial Campanario o a Terraplaza.")

calcular_costo_total()
