def verificar_bisiesto():
    year = int(input("Ingrese un año: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "es un año bisiesto.")
            else:
                print(year, "no es un año bisiesto.")
        else:
            print(year, "es un año bisiesto.")
    else:
        print(year, "no es un año bisiesto.")

verificar_bisiesto()
