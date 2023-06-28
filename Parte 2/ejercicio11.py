def verificar_pico_placa():
    placa = input("Ingrese el último dígito de la placa del vehículo: ")
    placa = int(placa)

    dia = input("Ingrese el día de la semana: ").lower()

    restriccion = False 

    if dia == "sábado" or dia == "domingo":
        restriccion = False
    elif dia == "lunes":
        if placa == 1 or placa == 2:
            restriccion = True
    elif dia == "martes":
        if placa == 3 or placa == 4:
            restriccion = True
    elif dia == "miércoles":
        if placa == 5 or placa == 6:
            restriccion = True
    elif dia == "jueves":
        if placa == 7 or placa == 8:
            restriccion = True
    elif dia == "viernes":
        if placa == 9 or placa == 0:
            restriccion = True
    else:
        print("El día ingresado no es válido.")

    if restriccion:
        print("El vehículo con placa terminada en", placa, "tiene restricción de pico y placa.")
    else:
        print("El vehículo con placa terminada en", placa, "puede circular libremente.")

verificar_pico_placa()
