# Curso python_basico #7

def ejemplo():
    print("Esta es una funcion en python")
    print("Hola como estas?")
    return 5+7
valor = ejemplo()
print(valor)
#ejemplo()

def suma(numero1, numero2):
    operacion = numero1 + numero2
    return operacion

def resta(numero1,numero2 ):
    operacion = numero1 - numero2
    return operacion

def multiplicacion(numero1, numero2):
    operacion = numero1*numero2
    return operacion

def divsion(numero1, numero2):
    #operacion = numero1//numero2  retorna division entera con (//) y (/ con decimal)
   # operacion = numero1/numero2
    return numero1//numero2

def nombre(myNombre):
    print("Hola mi nombre es: ",myNombre)

resultado = suma(10,5)
print(resultado)
#print(suma(2,8))  otra opcion para varias sumas, con una funcion y solamente pasando parametros
#print(suma(3,8))

resultado=resta(8,5)
print(resultado)

#resultado = multiplicacion(5,5)
#print(resultado)
print(multiplicacion(5,5))

resultado = divsion(16,4)
print(resultado)

nombre("gladys")

