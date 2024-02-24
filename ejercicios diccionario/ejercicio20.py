class AdministradorEventos:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar información de los eventos
        self.eventos = {}

    def agregar_evento(self, nombre_evento, fecha, hora, participantes=None):
        # Agregar un evento al diccionario
        if nombre_evento not in self.eventos:
            self.eventos[nombre_evento] = {'fecha': fecha, 'hora': hora, 'participantes': participantes or []}
            print(f"Evento '{nombre_evento}' agregado para el {fecha} a las {hora}.")
        else:
            print(f"El evento '{nombre_evento}' ya existe.")

    def agregar_participante(self, nombre_evento, participante):
        # Agregar un participante a un evento existente
        evento = self.eventos.get(nombre_evento, None)
        if evento:
            participantes = evento['participantes']
            if participante not in participantes:
                participantes.append(participante)
                print(f"Participante '{participante}' agregado al evento '{nombre_evento}'.")
            else:
                print(f"El participante '{participante}' ya está registrado para el evento '{nombre_evento}'.")
        else:
            print(f"No se encontró el evento '{nombre_evento}'.")

    def obtener_info_evento(self, nombre_evento):
        # Obtener información de un evento por su nombre
        return self.eventos.get(nombre_evento, None)

    def obtener_todos_los_eventos(self):
        # Devolver todos los eventos y su información
        return self.eventos

# Ejemplo de uso
administrador_eventos = AdministradorEventos()

# Agregar eventos al diccionario
administrador_eventos.agregar_evento('Reunión de equipo', '2024-02-22', '10:00', ['Juan', 'María'])
administrador_eventos.agregar_evento('Presentación de Proyecto', '2024-02-25', '15:30', ['Pedro', 'Ana'])

# Agregar participantes a un evento existente
administrador_eventos.agregar_participante('Reunión de equipo', 'Carlos')

# Obtener información de un evento
info_evento = administrador_eventos.obtener_info_evento('Reunión de equipo')
print("Información de la Reunión de equipo:", info_evento)

# Obtener todos los eventos y su información
todos_los_eventos = administrador_eventos.obtener_todos_los_eventos()
print("Todos los eventos:", todos_los_eventos)