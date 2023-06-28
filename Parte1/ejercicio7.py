def calcular_iva():
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    descuento = float(input("Ingrese el descuento en porcentaje: "))

    
    descuento_valor = precio * (descuento / 100)
    subtotal = precio - descuento_valor
    iva = subtotal * 0.19
    total = subtotal + iva

    print("\nFactura:")
    print("Producto:", nombre_producto)
    print("Precio: $", precio)
    print("Descuento: $", descuento_valor)
    print("Subtotal: $", subtotal)
    print("IVA (19%): $", iva)
    print("Total a pagar: $", total)

calcular_iva()
