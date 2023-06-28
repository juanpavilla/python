distancia = float(input("Ingrese la distancia: "))

if distancia > 20 and distancia < 35:
    tiempo = float(input("Ingrese el tiempo: "))
    velocidad = distancia / tiempo
    print("La velocidad es:", velocidad)
else:
    print("La distancia no cumple con los criterios establecidos.")
