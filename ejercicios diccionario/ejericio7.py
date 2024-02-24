class ConvertidorUnidades:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar las conversiones
        self.conversiones = {}

    def agregar_conversion(self, unidad_origen, unidad_destino, factor_conversion):
        # Agregar una conversión al diccionario
        clave = (unidad_origen, unidad_destino)
        self.conversiones[clave] = factor_conversion

    def realizar_conversion(self, valor, unidad_origen, unidad_destino):
        # Realizar una conversión de unidad
        clave = (unidad_origen, unidad_destino)
        factor_conversion = self.conversiones.get(clave, None)
        if factor_conversion is not None:
            resultado = valor * factor_conversion
            return resultado
        else:
            print(f"No se encontró una conversión de {unidad_origen} a {unidad_destino} en el diccionario.")
            return None

# Ejemplo de uso
convertidor = ConvertidorUnidades()

# Agregar conversiones al diccionario
convertidor.agregar_conversion('kilometros', 'millas', 0.621371)
convertidor.agregar_conversion('metros', 'pies', 3.28084)
convertidor.agregar_conversion('litros', 'galones', 0.264172)

# Realizar conversiones
resultado1 = convertidor.realizar_conversion(10, 'kilometros', 'millas')
print("10 kilómetros en millas:", resultado1)

resultado2 = convertidor.realizar_conversion(20, 'metros', 'pies')
print("20 metros en pies:", resultado2)

resultado3 = convertidor.realizar_conversion(30, 'litros', 'galones')
print("30 litros en galones:", resultado3)

resultado4 = convertidor.realizar_conversion(15, 'millas', 'kilometros')  # Esta conversión no está en el diccionario