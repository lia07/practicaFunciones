# Invertir un número ( Ejm: entrada = 123, salida=321)
numero_ingresado = (input("Ingrese un número: "))
invertir = 0
try:
    valor = int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
        invertir = (invertir * 10) + residuo
        valor //= 10
    print('El inverso del número ingresado es: ', invertir)
except ValueError:
  print("Ese número no es valido. Inténtalo de nevo !")