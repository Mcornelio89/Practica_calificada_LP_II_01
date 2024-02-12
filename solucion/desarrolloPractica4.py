class Tarea:
    def __init__(tarea, descripcion, completada=False):
        tarea.descripcion = descripcion
        tarea.completada = completada

class AdministradorTareas:
    def __init__(administrador):
        administrador.tareas = []

    def añadir_tarea(administrador, descripcion):
        nueva_tarea = Tarea(descripcion)
        administrador.tareas.append(nueva_tarea)
        print(f'Tarea "{descripcion}" añadida.')

    def eliminar_tarea(administrador, indice):
        if 0 <= indice < len(administrador.tareas):
            tarea_eliminada = administrador.tareas.pop(indice)
            print(f'Tarea "{tarea_eliminada.descripcion}" eliminada.')
        else:
            print('Índice de tarea no válido.')

    def mostrar_todas_las_tareas(administrador):
        if not administrador.tareas:
            print('No hay tareas.')
        else:
            for i, tarea in enumerate(administrador.tareas):
                estado = 'Completada' if tarea.completada else 'Pendiente'
                print(f'{i + 1}. {tarea.descripcion} - {estado}')

    def marcar_como_completada(administrador, indice):
        if 0 <= indice < len(administrador.tareas):
            tarea = administrador.tareas[indice]
            tarea.completada = True
            print(f'Tarea "{tarea.descripcion}" marcada como completada.')
        else:
            print('Índice de tarea no válido.')


# Función principal para interactuar con el usuario
def main():
    administrador = AdministradorTareas()

    while True:
        print('\n----- Administrador de Tareas -----')
        print('1. Añadir Tarea')
        print('2. Eliminar Tarea')
        print('3. Mostrar Todas las Tareas')
        print('4. Marcar Tarea como Completada')
        print('5. Salir')

        opcion = input('Selecciona una opción (1-5): ')

        if opcion == '1':
            descripcion = input('Ingrese la descripción de la tarea: ')
            AdministradorTareas.añadir_tarea(administrador, descripcion)
        elif opcion == '2':
            indice = int(input('Ingrese el índice de la tarea a eliminar: '))
            AdministradorTareas.eliminar_tarea(administrador, indice - 1)
        elif opcion == '3':
            AdministradorTareas.mostrar_todas_las_tareas(administrador)
        elif opcion == '4':
            indice = int(input('Ingrese el índice de la tarea a marcar como completada: '))
            AdministradorTareas.marcar_como_completada(administrador, indice - 1)
        elif opcion == '5':
            print('Saliendo del Administrador de Tareas. ¡Hasta luego!')
            break
        else:
            print('Opción no válida. Inténtelo de nuevo.')

if __name__ == "__main__":
    main()