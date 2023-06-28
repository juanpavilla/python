def intercambiar_valores():
    a = input("Ingrese el valor de a: ")
    b = input("Ingrese el valor de b: ")

    print("Valores originales: a =", a, "b =", b)
    
    aux = a
    a = b
    b = aux

    print("Valores intercambiados: a =", a, "b =", b)

intercambiar_valores()
