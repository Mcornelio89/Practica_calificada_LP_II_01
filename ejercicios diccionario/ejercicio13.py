class ConfiguracionApp:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar las configuraciones
        self.configuraciones = {}

    def agregar_configuracion(self, clave, valor):
        # Agregar una configuración al diccionario
        self.configuraciones[clave] = valor

    def obtener_configuracion(self, clave):
        # Obtener el valor de una configuración por su clave
        return self.configuraciones.get(clave, None)

    def actualizar_configuracion(self, clave, nuevo_valor):
        # Actualizar el valor de una configuración por su clave
        if clave in self.configuraciones:
            self.configuraciones[clave] = nuevo_valor
        else:
            print(f"No se encontró la configuración con la clave {clave}.")

    def eliminar_configuracion(self, clave):
        # Eliminar una configuración por su clave
        if clave in self.configuraciones:
            del self.configuraciones[clave]
        else:
            print(f"No se encontró la configuración con la clave {clave}.")

    def obtener_todas_las_configuraciones(self):
        # Devolver todas las configuraciones en el diccionario
        return self.configuraciones

# Ejemplo de uso
configuracion_app = ConfiguracionApp()

# Agregar configuraciones al diccionario
configuracion_app.agregar_configuracion('idioma', 'español')
configuracion_app.agregar_configuracion('tema', 'oscuro')
configuracion_app.agregar_configuracion('notificaciones', True)

# Obtener el valor de una configuración
idioma = configuracion_app.obtener_configuracion('idioma')
print("Idioma:", idioma)

# Actualizar el valor de una configuración
configuracion_app.actualizar_configuracion('tema', 'claro')

# Eliminar una configuración
configuracion_app.eliminar_configuracion('notificaciones')

# Obtener todas las configuraciones
todas_las_configuraciones = configuracion_app.obtener_todas_las_configuraciones()
print("Todas las configuraciones:", todas_las_configuraciones)