def generador_potencia(base):
    print("base: ", base)
    def decorator(f):
        print("f: ", f.__name__)
        def inner(n):
            print('n: ', n)
            exponente = f(n) # se ejecuta la funcion retornando n
            potencia = base**exponente
            return potencia
        return inner
    return decorator

@generador_potencia(3) # para este caso la abase es 3
def funcion_exponente(n):
    return n

texto = 'Decorador para 3**2:'
res = funcion_exponente(2) #se ejecuta la funcion inner
print(texto, res)
