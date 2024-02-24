class ManejadorDiccionario:
    def __init__(self):
        # Inicializar un diccionario vacío
        self.diccionario = {}

    def agregar_par(self, clave, valor):
        # Agregar un par clave-valor al diccionario
        self.diccionario[clave] = valor

    def actualizar_par(self, clave, nuevo_valor):
        # Actualizar el valor de un par clave-valor existente
        if clave in self.diccionario:
            self.diccionario[clave] = nuevo_valor
        else:
            print(f"La clave '{clave}' no existe en el diccionario.")

    def eliminar_par(self, clave):
        # Eliminar un par clave-valor del diccionario
        if clave in self.diccionario:
            del self.diccionario[clave]
        else:
            print(f"La clave '{clave}' no existe en el diccionario.")

# Ejemplo de uso
manejador = ManejadorDiccionario()

manejador.agregar_par("nombre", "Juan")
manejador.agregar_par("edad", 25)

print("Diccionario actual:", manejador.diccionario)

manejador.actualizar_par("edad", 26)
print("Diccionario actualizado:", manejador.diccionario)

manejador.eliminar_par("nombre")
print("Diccionario después de eliminar 'nombre':", manejador.diccionario)