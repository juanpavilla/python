def calcular_salario():
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    valor_hora = float(input("Ingrese el valor de la hora: "))

    if horas_trabajadas <= 35:
        salario = horas_trabajadas * valor_hora
    else:
        horas_extra = horas_trabajadas - 35
        salario = (35 * valor_hora) + (horas_extra * valor_hora * 1.5)

    print("El empleado", nombre, "tiene un salario de:", salario)

calcular_salario()
