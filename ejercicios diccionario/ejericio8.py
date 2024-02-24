class AdministradorCalificaciones:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar las calificaciones de los estudiantes
        self.calificaciones = {}

    def agregar_calificacion(self, estudiante, asignatura, calificacion):
        # Agregar una calificación al diccionario
        if estudiante not in self.calificaciones:
            self.calificaciones[estudiante] = {}
        self.calificaciones[estudiante][asignatura] = calificacion

    def obtener_calificacion(self, estudiante, asignatura):
        # Obtener la calificación de un estudiante en una asignatura
        if estudiante in self.calificaciones and asignatura in self.calificaciones[estudiante]:
            return self.calificaciones[estudiante][asignatura]
        else:
            print(f"No se encontró la calificación de {estudiante} en {asignatura}.")
            return None

    def obtener_calificaciones_estudiante(self, estudiante):
        # Obtener todas las calificaciones de un estudiante
        return self.calificaciones.get(estudiante, None)

    def obtener_calificaciones_asignatura(self, asignatura):
        # Obtener las calificaciones de todos los estudiantes en una asignatura
        calificaciones_asignatura = {}
        for estudiante, calificaciones in self.calificaciones.items():
            if asignatura in calificaciones:
                calificaciones_asignatura[estudiante] = calificaciones[asignatura]
        return calificaciones_asignatura

# Ejemplo de uso
admin_calificaciones = AdministradorCalificaciones()

# Agregar calificaciones al diccionario
admin_calificaciones.agregar_calificacion('Juan', 'Matemáticas', 18)
admin_calificaciones.agregar_calificacion('Juan', 'Historia', 17)
admin_calificaciones.agregar_calificacion('María', 'Matemáticas', 18)
admin_calificaciones.agregar_calificacion('María', 'Historia', 18)

# Obtener calificación de un estudiante en una asignatura
calificacion_juan_matematicas = admin_calificaciones.obtener_calificacion('Juan', 'Matemáticas')
print("Calificación de Juan en Matemáticas:", calificacion_juan_matematicas)

# Obtener todas las calificaciones de un estudiante
calificaciones_maria = admin_calificaciones.obtener_calificaciones_estudiante('María')
print("Calificaciones de María:", calificaciones_maria)

# Obtener calificaciones de todos los estudiantes en una asignatura
calificaciones_historia = admin_calificaciones.obtener_calificaciones_asignatura('Historia')
print("Calificaciones de Historia:", calificaciones_historia)