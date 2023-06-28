decimal = int(input("Ingrese un número decimal para pasar a Binario: "))

binario = ""
octal = ""
hexadecimal = ""

while decimal > 0:
    residuo = decimal % 2
    binario = str(residuo) + binario
    decimal = decimal // 2


decimal = int(input("Ingrese un número decimal para pasarlo a Octal: "))
while decimal > 0:
    residuo = decimal % 8
    octal = str(residuo) + octal
    decimal = decimal // 8


decimal = int(input("Ingrese un número decimal para pasarlo a Hexadecimal: "))
while decimal > 0:
    residuo = decimal % 16
    hexadecimal = hex(residuo).lstrip("0x") + hexadecimal
    decimal = decimal // 16

print("El número binario equivalente es:", binario)
print("El número octal equivalente es:", octal)
print("El número hexadecimal equivalente es:", hexadecimal)
