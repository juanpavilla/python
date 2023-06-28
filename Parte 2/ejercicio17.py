
nombre = input("Ingrese el nombre del estudiante: ")
calificacion = float(input("Ingrese la calificación del estudiante (entre 0 y 100): "))


if calificacion >= 90:
    nota = "A"
elif calificacion < 90 and calificacion >= 80:
    nota = "B"
elif calificacion < 80 and calificacion >= 70:
    nota = "C"
elif calificacion < 70 and calificacion >= 69:
    nota = "D"
else:

    nota = "F"

print("La calificación de", nombre, "es", nota)
