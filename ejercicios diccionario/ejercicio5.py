class AgendaTelefonica:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar los contactos
        self.agenda = {}

    def agregar_contacto(self, nombre, telefono):
        # Agregar un contacto a la agenda
        self.agenda[nombre] = telefono

    def obtener_contacto(self, nombre):
        # Obtener el número de teléfono de un contacto por su nombre
        return self.agenda.get(nombre, None)

    def modificar_contacto(self, nombre, nuevo_telefono):
        # Modificar el número de teléfono de un contacto por su nombre
        if nombre in self.agenda:
            self.agenda[nombre] = nuevo_telefono
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")

    def eliminar_contacto(self, nombre):
        # Eliminar un contacto por su nombre
        if nombre in self.agenda:
            del self.agenda[nombre]
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")

    def obtener_todos_los_contactos(self):
        # Devolver todos los contactos en la agenda
        return self.agenda

# Ejemplo de uso
agenda_telefonica = AgendaTelefonica()

# Agregar contactos a la agenda
agenda_telefonica.agregar_contacto('Juan', '123-456-7890')
agenda_telefonica.agregar_contacto('María', '987-654-3210')

# Obtener el número de teléfono de un contacto
telefono_juan = agenda_telefonica.obtener_contacto('Juan')
print("Número de teléfono de Juan:", telefono_juan)

# Modificar el número de teléfono de un contacto
agenda_telefonica.modificar_contacto('Juan', '111-222-3333')

# Eliminar un contacto
agenda_telefonica.eliminar_contacto('María')

# Obtener todos los contactos en la agenda
todos_los_contactos = agenda_telefonica.obtener_todos_los_contactos()
print("Todos los contactos en la agenda:", todos_los_contactos)