class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

# Crear instancias de Perro y Gato
animal1 = Perro()
animal2 = Gato()

# Llamar al método hacer_sonido en objetos de ambas clases
print("El perro hace sonido:", animal1.hacer_sonido())
print("El gato hace sonido:", animal2.hacer_sonido())