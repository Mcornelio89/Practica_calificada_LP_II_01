class GestionadorTareas:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar las tareas
        self.tareas = {}
        # Inicializar un contador para generar identificadores únicos
        self.contador_id = 1

    def agregar_tarea(self, descripcion):
        # Agregar una tarea pendiente al diccionario
        id_tarea = self.contador_id
        self.tareas[id_tarea] = {'descripcion': descripcion, 'estado': 'pendiente'}
        self.contador_id += 1
        return id_tarea

    def marcar_como_realizada(self, id_tarea):
        # Marcar una tarea como realizada por su identificador
        tarea = self.tareas.get(id_tarea, None)
        if tarea:
            tarea['estado'] = 'realizada'
        else:
            print(f"La tarea con ID {id_tarea} no existe en la lista.")

    def obtener_tarea(self, id_tarea):
        # Obtener información de una tarea por su identificador
        return self.tareas.get(id_tarea, None)

    def obtener_todas_las_tareas(self):
        # Devolver todas las tareas en el diccionario
        return self.tareas

# Ejemplo de uso
gestor_tareas = GestionadorTareas()

# Agregar tareas a la lista
id_tarea1 = gestor_tareas.agregar_tarea('Hacer la compra')
id_tarea2 = gestor_tareas.agregar_tarea('Estudiar para el examen')

# Marcar una tarea como realizada
gestor_tareas.marcar_como_realizada(id_tarea1)

# Obtener información de una tarea
info_tarea2 = gestor_tareas.obtener_tarea(id_tarea2)
print("Información de la tarea 2:", info_tarea2)

# Obtener todas las tareas en la lista
todas_las_tareas = gestor_tareas.obtener_todas_las_tareas()
print("Todas las tareas:", todas_las_tareas)