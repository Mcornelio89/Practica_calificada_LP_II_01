class GestionadorHotel:
    def __init__(self, num_habitaciones):
        # Inicializar un diccionario para almacenar información de las habitaciones
        self.habitaciones = {}
        for num_hab in range(1, num_habitaciones + 1):
            self.habitaciones[num_hab] = {'disponible': True, 'reservado_por': None}

    def realizar_reservacion(self, num_habitacion, nombre_cliente):
        # Realizar una reservación en una habitación
        habitacion = self.habitaciones.get(num_habitacion, None)
        if habitacion:
            if habitacion['disponible']:
                habitacion['disponible'] = False
                habitacion['reservado_por'] = nombre_cliente
                print(f"Reservación realizada en la habitación {num_habitacion} por {nombre_cliente}.")
            else:
                print(f"La habitación {num_habitacion} ya está ocupada.")
        else:
            print(f"La habitación {num_habitacion} no existe en el hotel.")

    def cancelar_reservacion(self, num_habitacion):
        # Cancelar una reservación en una habitación
        habitacion = self.habitaciones.get(num_habitacion, None)
        if habitacion:
            if not habitacion['disponible']:
                habitacion['disponible'] = True
                habitacion['reservado_por'] = None
                print(f"Reservación cancelada en la habitación {num_habitacion}.")
            else:
                print(f"La habitación {num_habitacion} no está reservada.")
        else:
            print(f"La habitación {num_habitacion} no existe en el hotel.")

    def obtener_estado_habitaciones(self):
        # Devolver el estado actual de todas las habitaciones
        return self.habitaciones

# Ejemplo de uso
hotel = GestionadorHotel(num_habitaciones=10)

# Realizar reservaciones
hotel.realizar_reservacion(3, 'Juan')
hotel.realizar_reservacion(7, 'María')

# Cancelar una reservación
hotel.cancelar_reservacion(3)

# Obtener el estado actual de las habitaciones
estado_habitaciones = hotel.obtener_estado_habitaciones()
print("Estado actual de las habitaciones:", estado_habitaciones)