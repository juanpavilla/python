def descomposicion_factores_primos(numero):
    i = 2
    factores_primos = []

    while i <= numero:
        if numero % i == 0:
            factores_primos.append(i)
            numero = numero // i
        else:
            i += 1

    return factores_primos

k = int(input("Ingrese un número entero: "))
factores = descomposicion_factores_primos(k)
print("La descomposición en factores primos de", k, "es:")
for factor in factores:
    print(factor)
