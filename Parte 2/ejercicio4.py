def ordenar_numeros():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    if numero1 < numero2:
        menor = numero1
        mayor = numero2
    else:
        menor = numero2
        mayor = numero1

    print("Los numeros Ingresados son:", numero1, "y", numero2, " y Oganizados de menor a mayor son:", menor, "-", mayor)

ordenar_numeros()
