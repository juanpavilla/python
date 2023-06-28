def calcular_salario_impuestos():
    nombre = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    valor_hora = float(input("Ingrese el valor de la hora: "))

    if horas_trabajadas <= 35:
        salario = horas_trabajadas * valor_hora
    else:
        horas_extra = horas_trabajadas - 35
        salario = (35 * valor_hora) + (horas_extra * valor_hora * 1.5)

    if salario <= 2000:
        impuestos = 0
    elif salario <= 2500:
        impuestos = salario * 0.2
    else:
        impuestos = salario * 0.3

    salario_neto = salario - impuestos

    print("Empleado:", nombre)
    print("Salario bruto:", salario)
    print("Impuestos:", impuestos)
    print("Salario neto:", salario_neto)

calcular_salario_impuestos()
