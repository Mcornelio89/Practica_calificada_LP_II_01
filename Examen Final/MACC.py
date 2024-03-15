import json

# Clase base para representar a una persona
class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

# Clase derivada de Persona para representar a un comprador
class Comprador(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'email': self.email
        }

# Clase derivada de Persona para representar a un organizador
class Organizador(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

# Interfaz para eventos
class Evento:
    def __init__(self, nombre, fecha, lugar):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar

    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fecha: {self.fecha}")
        print(f"Lugar: {self.lugar}")
        pass

# Clase para eventos de parrillada
class EventoParrillada(Evento):
    def mostrar_detalle(self):
        print("Detalles del evento de parrillada")

# Clase para eventos VIP
class EventoVIP(Evento):
    def mostrar_detalle(self):
        print("Detalles del evento VIP")

# Clase para representar una venta
class Venta:
    def __init__(self, comprador, evento, cantidad_tickets):
        self.comprador = comprador
        self.evento = evento
        self.cantidad_tickets = cantidad_tickets

    def calcular_descuento(self):
        precio_base = 100  # Precio base por ticket
        descuento = 0

        # Implementación para calcular descuentos por volumen de compra
        if self.cantidad_tickets >= 10:
            descuento = 0.1 * precio_base * self.cantidad_tickets  # Descuento del 10% para más de 10 tickets

        return descuento

# Clase para gestionar las ventas
class GestorVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def reporte_ventas_por_evento(self):
        reporte = {}

        for venta in self.ventas:
            evento = venta.evento.nombre
            if evento in reporte:
                reporte[evento] += venta.cantidad_tickets
            else:
                reporte[evento] = venta.cantidad_tickets

        print("Reporte de ventas por evento:")
        for evento, cantidad in reporte.items():
            print(f"- {evento}: {cantidad} tickets vendidos")

    def reporte_ventas_totales(self):
        total_ventas = 0

        for venta in self.ventas:
            total_ventas += venta.cantidad_tickets

        print("Reporte de ventas totales:")
        print(f"Total de tickets vendidos: {total_ventas}")

    def guardar_ventas_json(self, filename):
        with open(filename, 'w') as file:
            ventas_dict = []
            for venta in self.ventas:
                venta_dict = {
                    'comprador': venta.comprador.to_dict(),
                    'evento': venta.evento.__dict__,
                    'cantidad_tickets': venta.cantidad_tickets
                }
                ventas_dict.append(venta_dict)
            json.dump(ventas_dict, file, indent=4)

    def cargar_ventas_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.ventas = [Venta(**venta) for venta in data]

# Excepciones personalizadas
class EventoAgotadoError(Exception):
    pass

class DatosInvalidosError(Exception):
    pass

class ProblemaArchivoError(Exception):
    pass

# Interfaz de usuario avanzada
def menu_principal():
    print("1. Comprar ticket")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def mostrar_eventos_disponibles(eventos):
    print("Eventos disponibles:")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento.nombre}")

def comprar_ticket(gestor_ventas, eventos):
    mostrar_eventos_disponibles(eventos)
    seleccion = input("Seleccione el número del evento al que desea comprar un ticket: ")
    
    try:
        seleccion = int(seleccion)
        if seleccion < 1 or seleccion > len(eventos):
            raise DatosInvalidosError("La opción seleccionada no es válida.")
        
        evento_seleccionado = eventos[seleccion - 1]
        cantidad_tickets = int(input("Ingrese la cantidad de tickets que desea comprar: "))
        if cantidad_tickets <= 0:
            raise DatosInvalidosError("La cantidad de tickets debe ser mayor que cero.")
        
        comprador_nombre = input("Ingrese su nombre: ")
        comprador_email = input("Ingrese su email: ")
        comprador = Comprador(comprador_nombre, comprador_email)
        
        venta = Venta(comprador, evento_seleccionado, cantidad_tickets)
        gestor_ventas.agregar_venta(venta)

        print(f"¡Compra realizada con éxito! Ha comprado {cantidad_tickets} tickets para el evento {evento_seleccionado.nombre}.")

    except ValueError:
        print("Error: La cantidad de tickets debe ser un número entero.")
    except DatosInvalidosError as e:
        print(f"Error: {e}")

def main():
    gestor_ventas = GestorVentas()
    eventos = [
        EventoParrillada("Parrillada Verano", "2024-07-15", "Parque Central"),
        EventoVIP("Fiesta VIP", "2024-08-20", "Hotel de Lujo"),
        EventoParrillada("Gran Barbacoa", "2024-09-10", "Estadio Municipal")
    ]

    while True:
        opcion = menu_principal()
        if opcion == "1":
            comprar_ticket(gestor_ventas, eventos)
        elif opcion == "2":
            gestor_ventas.guardar_ventas_json("ventas.json")
            print("Gracias por usar nuestro sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
