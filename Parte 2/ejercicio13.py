num1 = float(input("Ingrese el primer número del dado: "))
num2 = float(input("Ingrese el segundo número del dado: "))
num3 = float(input("Ingrese el tercer número del dado: "))

if num1 < num2 < num3 or num3 < num2 < num1:
    numero_central = num2
elif num2 < num1 < num3 or num3 < num1 < num2:
    numero_central = num1
else:
    numero_central = num3

print("El número central del dado es:", numero_central)
