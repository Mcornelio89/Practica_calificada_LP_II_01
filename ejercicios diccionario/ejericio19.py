class SistemaAlquilerVehiculos:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar información de los vehículos y su disponibilidad
        self.vehiculos = {}

    def agregar_vehiculo(self, id_vehiculo, modelo, disponibilidad=True):
        # Agregar un vehículo al diccionario
        if id_vehiculo not in self.vehiculos:
            self.vehiculos[id_vehiculo] = {'modelo': modelo, 'disponible': disponibilidad}
            print(f"Vehículo {modelo} agregado al sistema con ID {id_vehiculo}.")
        else:
            print(f"El vehículo con ID {id_vehiculo} ya existe en el sistema.")

    def consultar_disponibilidad(self, id_vehiculo):
        # Consultar la disponibilidad de un vehículo por su ID
        vehiculo = self.vehiculos.get(id_vehiculo, None)
        if vehiculo:
            return vehiculo['disponible']
        else:
            print(f"No se encontró el vehículo con ID {id_vehiculo}.")
            return None

    def alquilar_vehiculo(self, id_vehiculo):
        # Alquilar un vehículo por su ID
        vehiculo = self.vehiculos.get(id_vehiculo, None)
        if vehiculo:
            if vehiculo['disponible']:
                vehiculo['disponible'] = False
                print(f"Vehículo con ID {id_vehiculo} alquilado.")
            else:
                print(f"El vehículo con ID {id_vehiculo} no está disponible para alquilar.")
        else:
            print(f"No se encontró el vehículo con ID {id_vehiculo}.")

    def devolver_vehiculo(self, id_vehiculo):
        # Devolver un vehículo por su ID
        vehiculo = self.vehiculos.get(id_vehiculo, None)
        if vehiculo:
            if not vehiculo['disponible']:
                vehiculo['disponible'] = True
                print(f"Vehículo con ID {id_vehiculo} devuelto correctamente.")
            else:
                print(f"El vehículo con ID {id_vehiculo} ya está disponible.")
        else:
            print(f"No se encontró el vehículo con ID {id_vehiculo}.")

    def obtener_todos_los_vehiculos(self):
        # Devolver todos los vehículos en el sistema
        return self.vehiculos

# Ejemplo de uso
sistema_alquiler = SistemaAlquilerVehiculos()

# Agregar vehículos al sistema
sistema_alquiler.agregar_vehiculo(1, 'Sedán', True)
sistema_alquiler.agregar_vehiculo(2, 'SUV', True)
sistema_alquiler.agregar_vehiculo(3, 'Camioneta', False)

# Consultar disponibilidad de un vehículo
disponibilidad_vehiculo_1 = sistema_alquiler.consultar_disponibilidad(1)
print("Disponibilidad del vehículo 1:", disponibilidad_vehiculo_1)

# Alquilar un vehículo
sistema_alquiler.alquilar_vehiculo(2)

# Devolver un vehículo
sistema_alquiler.devolver_vehiculo(3)

# Obtener todos los vehículos en el sistema
todos_los_vehiculos = sistema_alquiler.obtener_todos_los_vehiculos()
print("Todos los vehículos en el sistema:", todos_los_vehiculos)