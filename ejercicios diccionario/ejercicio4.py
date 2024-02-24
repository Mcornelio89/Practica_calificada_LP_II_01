class InventarioProductos:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar la información de los productos
        self.inventario = {}

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        # Agregar un producto al inventario
        self.inventario[codigo] = {
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        }

    def obtener_producto(self, codigo):
        # Obtener la información de un producto por su código
        return self.inventario.get(codigo, None)

    def actualizar_cantidad(self, codigo, nueva_cantidad):
        # Actualizar la cantidad de un producto por su código
        producto = self.inventario.get(codigo, None)
        if producto:
            producto['cantidad'] = nueva_cantidad
        else:
            print(f"El producto con código {codigo} no existe en el inventario.")

    def actualizar_precio(self, codigo, nuevo_precio):
        # Actualizar el precio de un producto por su código
        producto = self.inventario.get(codigo, None)
        if producto:
            producto['precio'] = nuevo_precio
        else:
            print(f"El producto con código {codigo} no existe en el inventario.")

    def eliminar_producto(self, codigo):
        # Eliminar un producto por su código
        if codigo in self.inventario:
            del self.inventario[codigo]
        else:
            print(f"El producto con código {codigo} no existe en el inventario.")

    def obtener_todos_los_productos(self):
        # Devolver todos los productos en el inventario
        return self.inventario

# Ejemplo de uso
inventario_productos = InventarioProductos()

# Agregar productos al inventario
inventario_productos.agregar_producto(101, 'Camiseta', 50, 15.99)
inventario_productos.agregar_producto(102, 'Pantalón', 30, 29.99)

# Obtener información de un producto
producto_101 = inventario_productos.obtener_producto(101)
print("Información del producto 101:", producto_101)

# Actualizar la cantidad de un producto
inventario_productos.actualizar_cantidad(101, 45)

# Actualizar el precio de un producto
inventario_productos.actualizar_precio(102, 34.99)

# Eliminar un producto
inventario_productos.eliminar_producto(102)

# Obtener todos los productos en el inventario
todos_los_productos = inventario_productos.obtener_todos_los_productos()
print("Todos los productos en el inventario:", todos_los_productos)