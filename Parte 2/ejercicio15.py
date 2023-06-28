menos_40kg = 0
entre_40_50kg = 0
entre_50_60kg = 0
mas_60kg = 0


num_alumnos = int(input("Ingrese el número de alumnos: "))


for i in range(num_alumnos):
    peso = float(input(f"Ingrese el peso del alumno {i+1}: "))

    if peso < 40:
        menos_40kg += 1
    elif 40 <= peso <= 50:
        entre_40_50kg += 1
    elif 50 < peso < 60:
        entre_50_60kg += 1
    elif peso >= 60:
        mas_60kg += 1


print("Estadísticas de pesos de los alumnos:")
print("Alumnos de menos de 40 kg:", menos_40kg)
print("Alumnos entre 40 y 50 kg:", entre_40_50kg)
print("Alumnos de más de 50 kg y menos de 60 kg:", entre_50_60kg)
print("Alumnos de más o igual a 60 kg:", mas_60kg)
