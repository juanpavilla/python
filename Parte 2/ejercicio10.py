def calcular_area_triangulo():
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))

    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
        semiperimetro = (lado1 + lado2 + lado3) / 2
        area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5

        print("El área del triángulo es:", area)
    else:
        print("Los lados ingresados no corresponden a un triángulo válido.")

calcular_area_triangulo()
