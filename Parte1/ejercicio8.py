def convertir_tamaño():
    megabytes = float(input("Ingrese el tamaño en Megabytes: "))
    bits = megabytes * 8 * 1024 * 1024
    bytes = megabytes * 1024 * 1024
    kilobytes = megabytes * 1024
    gigabytes = megabytes / 1024

    print("Equivalencias:")
    print("Bits:", bits)
    print("Bytes:", bytes)
    print("Kilobytes:", kilobytes)
    print("Gigabytes:", gigabytes)

convertir_tamaño()
