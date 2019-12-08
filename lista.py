cantidad = int(input("Ingrese la cantidad de alumnos:"))
lista = []
grupo_a = []
grupo_b = []
alumno = {}
for n in range(cantidad):
    nombre = input("Ingrese nombre del alumno:")
    genero = input("Ingrese el genero 'M' o 'F':")
    alumno['nombre'] = nombre
    alumno['genero'] = genero
    lista.append(alumno)
    if lista[n]['genero'].lower()=='m':
        if lista[n]['nombre'].lower()<'m':
            grupo_a.append(lista[n]['nombre'])
        else:
            grupo_b.append(lista[n]['nombre'])
    if lista[n]['genero'].lower() == 'f':
        if lista[n]['nombre'].lower()<'m':
            grupo_b.append(lista[n]['nombre'])
        else:
            grupo_a.append(lista[n]['nombre'])

print("La lista de alumnos es", lista)
print("Alumnos de grupo A", grupo_a)
print("Alumnos de grupo B", grupo_b)