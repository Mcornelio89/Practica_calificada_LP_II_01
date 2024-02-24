class RegistroActividadesDiarias:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar las actividades diarias
        self.actividades_diarias = {}

    def agregar_actividad(self, fecha, actividad, duracion):
        # Agregar una actividad al diccionario
        if fecha not in self.actividades_diarias:
            self.actividades_diarias[fecha] = []
        self.actividades_diarias[fecha].append({'actividad': actividad, 'duracion': duracion})

    def obtener_actividades_por_fecha(self, fecha):
        # Obtener las actividades de una fecha específica
        return self.actividades_diarias.get(fecha, None)

    def obtener_todas_las_actividades(self):
        # Devolver todas las actividades registradas
        return self.actividades_diarias

# Ejemplo de uso
registro_actividades = RegistroActividadesDiarias()

# Agregar actividades al diccionario
registro_actividades.agregar_actividad('2024-02-22', 'Ejercicio', 60)
registro_actividades.agregar_actividad('2024-02-22', 'Estudio', 120)
registro_actividades.agregar_actividad('2024-02-23', 'Lectura', 45)

# Obtener actividades por fecha
actividades_fecha_22_feb = registro_actividades.obtener_actividades_por_fecha('2024-02-22')
print("Actividades del 22 de febrero:", actividades_fecha_22_feb)

# Obtener todas las actividades registradas
todas_las_actividades = registro_actividades.obtener_todas_las_actividades()
print("Todas las actividades registradas:", todas_las_actividades)