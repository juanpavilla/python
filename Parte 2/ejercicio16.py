
grados = float(input("Ingrese un ángulo en grados: "))

if grados < 90:
    tipo_angulo = "agudo"
elif grados == 90:
    tipo_angulo = "recto"
else:
    tipo_angulo = "obtuso"


print("El ángulo es", tipo_angulo)
