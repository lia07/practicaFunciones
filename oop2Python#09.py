#Programacion Orientado a Objetos #8
class Persona:
    def __init__(self):
        self.Nombre = nombre
        self.Edad = edad
        self.estado = "Vivo"
        print("Estoy de pie")
    def sentado(self):
        print("Estoy sentado")
    def estado_m(self):
        print("...")
    def descripcion(self):
        print("Hola me llamo", self.Nombre, "y tengo", self.Edad, "estoy", self.estado)

p1=Persona("Gladys", 25)

p1.dePie()
p1.sentado()
p1.estado_m()

p2 = Persona()
p2.dePie()
p2.sentado()
p2.estado_m()