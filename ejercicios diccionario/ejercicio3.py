class BaseDeDatosEstudiantes:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar la información de los estudiantes
        self.base_datos = {}

    def agregar_estudiante(self, id_estudiante, nombre, edad, notas):
        # Agregar un estudiante al diccionario de la base de datos
        self.base_datos[id_estudiante] = {
            'nombre': nombre,
            'edad': edad,
            'notas': notas
        }

    def obtener_estudiante(self, id_estudiante):
        # Obtener la información de un estudiante por su ID
        return self.base_datos.get(id_estudiante, None)

    def actualizar_notas(self, id_estudiante, nuevas_notas):
        # Actualizar las notas de un estudiante por su ID
        estudiante = self.base_datos.get(id_estudiante, None)
        if estudiante:
            estudiante['notas'] = nuevas_notas
        else:
            print(f"El estudiante con ID {id_estudiante} no existe en la base de datos.")

    def eliminar_estudiante(self, id_estudiante):
        # Eliminar un estudiante por su ID
        if id_estudiante in self.base_datos:
            del self.base_datos[id_estudiante]
        else:
            print(f"El estudiante con ID {id_estudiante} no existe en la base de datos.")

    def obtener_todos_los_estudiantes(self):
        # Devolver todos los estudiantes en la base de datos
        return self.base_datos

# Ejemplo de uso
base_datos_estudiantes = BaseDeDatosEstudiantes()

# Agregar estudiantes a la base de datos
base_datos_estudiantes.agregar_estudiante(1, 'Juan', 20, [18, 17, 16])
base_datos_estudiantes.agregar_estudiante(2, 'María', 22, [19, 18, 18])

# Obtener información de un estudiante
estudiante_1 = base_datos_estudiantes.obtener_estudiante(1)
print("Información del estudiante 1:", estudiante_1)

# Actualizar las notas de un estudiante
base_datos_estudiantes.actualizar_notas(1, [18, 17, 16])

# Eliminar un estudiante
base_datos_estudiantes.eliminar_estudiante(2)

# Obtener todos los estudiantes en la base de datos
todos_los_estudiantes = base_datos_estudiantes.obtener_todos_los_estudiantes()
print("Todos los estudiantes en la base de datos:", todos_los_estudiantes)