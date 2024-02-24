class GestorProyectos:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar información de los proyectos
        self.proyectos = {}

    def crear_proyecto(self, nombre_proyecto, miembros):
        # Crear un nuevo proyecto en el diccionario
        if nombre_proyecto not in self.proyectos:
            self.proyectos[nombre_proyecto] = {'miembros': miembros, 'tareas': {}}
            print(f"Proyecto '{nombre_proyecto}' creado con los miembros: {miembros}")
        else:
            print(f"El proyecto '{nombre_proyecto}' ya existe.")

    def agregar_miembro(self, nombre_proyecto, nuevo_miembro):
        # Agregar un nuevo miembro a un proyecto existente
        proyecto = self.proyectos.get(nombre_proyecto, None)
        if proyecto:
            miembros = proyecto['miembros']
            if nuevo_miembro not in miembros:
                miembros.append(nuevo_miembro)
                print(f"Nuevo miembro '{nuevo_miembro}' agregado al proyecto '{nombre_proyecto}'.")
            else:
                print(f"El miembro '{nuevo_miembro}' ya pertenece al proyecto '{nombre_proyecto}'.")
        else:
            print(f"No se encontró el proyecto '{nombre_proyecto}'.")

    def agregar_tarea(self, nombre_proyecto, tarea, asignado_a):
        # Agregar una tarea a un proyecto existente
        proyecto = self.proyectos.get(nombre_proyecto, None)
        if proyecto:
            tareas = proyecto['tareas']
            if tarea not in tareas:
                tareas[tarea] = {'asignado_a': asignado_a, 'estado': 'pendiente'}
                print(f"Tarea '{tarea}' agregada al proyecto '{nombre_proyecto}' y asignada a '{asignado_a}'.")
            else:
                print(f"La tarea '{tarea}' ya existe en el proyecto '{nombre_proyecto}'.")
        else:
            print(f"No se encontró el proyecto '{nombre_proyecto}'.")

    def obtener_info_proyecto(self, nombre_proyecto):
        # Obtener información de un proyecto por su nombre
        return self.proyectos.get(nombre_proyecto, None)

    def obtener_todos_los_proyectos(self):
        # Devolver todos los proyectos y su información
        return self.proyectos

# Ejemplo de uso
gestor_proyectos = GestorProyectos()

# Crear proyectos
gestor_proyectos.crear_proyecto('Proyecto1', ['Juan', 'María'])
gestor_proyectos.crear_proyecto('Proyecto2', ['Pedro', 'Ana'])

# Agregar miembros a un proyecto existente
gestor_proyectos.agregar_miembro('Proyecto1', 'Carlos')

# Agregar tareas a un proyecto existente
gestor_proyectos.agregar_tarea('Proyecto2', 'Desarrollar función de registro', 'Pedro')

# Obtener información de un proyecto
info_proyecto1 = gestor_proyectos.obtener_info_proyecto('Proyecto1')
print("Información del Proyecto1:", info_proyecto1)

# Obtener todos los proyectos y su información
todos_los_proyectos = gestor_proyectos.obtener_todos_los_proyectos()
print("Todos los proyectos:", todos_los_proyectos)