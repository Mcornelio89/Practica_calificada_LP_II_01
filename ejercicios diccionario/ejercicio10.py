class GestionadorEmpleados:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar la información de los empleados
        self.empleados = {}

    def agregar_empleado(self, id_empleado, nombre, posicion, salario):
        # Agregar un empleado al diccionario
        self.empleados[id_empleado] = {
            'nombre': nombre,
            'posicion': posicion,
            'salario': salario
        }

    def obtener_empleado(self, id_empleado):
        # Obtener la información de un empleado por su ID
        return self.empleados.get(id_empleado, None)

    def actualizar_salario(self, id_empleado, nuevo_salario):
        # Actualizar el salario de un empleado por su ID
        empleado = self.empleados.get(id_empleado, None)
        if empleado:
            empleado['salario'] = nuevo_salario
        else:
            print(f"El empleado con ID {id_empleado} no existe en la lista.")

    def eliminar_empleado(self, id_empleado):
        # Eliminar un empleado por su ID
        if id_empleado in self.empleados:
            del self.empleados[id_empleado]
        else:
            print(f"El empleado con ID {id_empleado} no existe en la lista.")

    def obtener_todos_los_empleados(self):
        # Devolver todos los empleados en el diccionario
        return self.empleados

# Ejemplo de uso
gestor_empleados = GestionadorEmpleados()

# Agregar empleados al diccionario
gestor_empleados.agregar_empleado(1, 'Juan', 'Desarrollador', 60000)
gestor_empleados.agregar_empleado(2, 'María', 'Diseñadora', 55000)

# Obtener información de un empleado por su ID
empleado_juan = gestor_empleados.obtener_empleado(1)
print("Información de Juan:", empleado_juan)

# Actualizar el salario de un empleado
gestor_empleados.actualizar_salario(2, 58000)

# Eliminar un empleado
gestor_empleados.eliminar_empleado(1)

# Obtener todos los empleados en el diccionario
todos_los_empleados = gestor_empleados.obtener_todos_los_empleados()
print("Todos los empleados:", todos_los_empleados)