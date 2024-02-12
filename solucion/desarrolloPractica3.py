asientos = []

def visualizar_asientos():
    print("Visualizando asientos")
    for fila in asientos:
        print(" ".join(fila))
    print()

def reservar_asientos():
    print("Reservando asiento")
    fila = int(input("Ingrese el número de fila: "))
    columna = int(input("Ingrese el número de columna: "))
    
    if asientos[fila - 1][columna - 1] == "X":
        print("Este asiento ya está reservado. Por favor, elija otro.")
    else:
        asientos[fila - 1][columna - 1] = "X"
        print("Reserva exitosa.")
    
    print()

def cancelar_reserva():
    print("Cancelando reserva")
    fila = int(input("Ingrese el número de fila: "))
    columna = int(input("Ingrese el número de columna: "))
    
    if asientos[fila - 1][columna - 1] == "X":
        asientos[fila - 1][columna - 1] = ""
        print("Cancelación de reserva exitosa.")
    else:
        print("Este asiento no está reservado. No se puede cancelar.")
    
    print()

def mostrar_menu():
    print("1. Visualizar asientos")
    print("2. Reservar asientos")
    print("3. Cancelar reserva")
    print("4. Salir")

def mostrar_estadisticas():
    total_asientos = sum(len(fila) for fila in asientos)
    asientos_ocupados = sum(fila.count("X") for fila in asientos)
    asientos_disponibles = total_asientos - asientos_ocupados

    porcentaje_ocupacion = (asientos_ocupados / total_asientos) * 100

    print(f"Estadísticas de ocupación:")
    print(f"Asientos ocupados: {asientos_ocupados}")
    print(f"Asientos disponibles: {asientos_disponibles}")
    print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")
    print()

def main():
    global asientos
    filas = int(input("Ingrese el número de filas en la sala de cine: "))
    columnas = int(input("Ingrese el número de columnas en la sala de cine: "))

    # Inicializar la sala de cine con asientos disponibles
    asientos = [["" for _ in range(columnas)] for _ in range(filas)]

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            visualizar_asientos()
        elif opcion == 2:
            reservar_asientos()
        elif opcion == 3:
            cancelar_reserva()
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

    mostrar_estadisticas()

if __name__ == "__main__":
    main()