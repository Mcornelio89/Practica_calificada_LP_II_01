from datetime import datetime

class SeguimientoHabitos:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar el seguimiento de hábitos
        self.seguimiento = {}

    def registrar_habito(self, habito, cumplido):
        # Registrar el seguimiento de un hábito en la fecha actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        
        if fecha_actual not in self.seguimiento:
            self.seguimiento[fecha_actual] = {}
        
        self.seguimiento[fecha_actual][habito] = cumplido

    def obtener_estado_habitual(self, fecha):
        # Obtener el estado de hábitos en una fecha específica
        return self.seguimiento.get(fecha, None)

    def obtener_todas_las_fechas(self):
        # Devolver todas las fechas registradas
        return list(self.seguimiento.keys())

# Ejemplo de uso
seguimiento_habitos = SeguimientoHabitos()

# Registrar hábitos
seguimiento_habitos.registrar_habito('Hacer ejercicio', True)
seguimiento_habitos.registrar_habito('Leer 30 minutos', False)
seguimiento_habitos.registrar_habito('Beber suficiente agua', True)

# Obtener el estado de hábitos en una fecha específica
estado_habitos_hoy = seguimiento_habitos.obtener_estado_habitual(datetime.now().strftime('%Y-%m-%d'))
print("Estado de hábitos hoy:", estado_habitos_hoy)

# Obtener todas las fechas registradas
todas_las_fechas = seguimiento_habitos.obtener_todas_las_fechas()
print("Todas las fechas registradas:", todas_las_fechas)