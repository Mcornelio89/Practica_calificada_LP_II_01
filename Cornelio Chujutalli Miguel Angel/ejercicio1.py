#1.Agregar producto
#2.Eliminar producto
#3.Actualizar producto
#4.Buscar producto
#5.Salir

print("\n1.Agregar producto.\n2.Eliminar producto.\n3.Actualizar producto.\n4.Buscar producto.\n4.Salir")
opcionUsuario = int(input("Opción   :   "))

listaProductos = []

if opcionUsuario == 1:
    cantidadProductos = int(input("Ingrese la cantidad de productos:"))
while cantidadProductos < 0:
    cantidadProductos = int(input("Ingrese la cantidad de productos:"))
for i in range (cantidadProductos):
    print ("Producto #", i +1)
    IDproducto = input ("Ingrese el IDproducto:")
    nombre = input ("Ingrese el nombre del producto:")
    cantidad = float (input("Ingrese la cantidad:"))
    precio = float (input("Ingrese el precio:"))
    valorInventario = cantidad*precio
    while precio <= 0:
        print("!!El precio no puede ser negativo!!")
        precio = float (input("Ingrese el precio:"))
    listaProductos.append([IDproducto,nombre,cantidad,precio,valorInventario])
    print ("Producto registrado")
print ("lista de Productos y valor total:")
for producto in listaProductos:
    print (f"IDproducto: {producto[0]} - nombre: {producto [1]} - cantidad: {producto [2]} - precio: {producto [3]} - valor de inventario: {producto [4]}")
elif opcionUsuario == 2:
    
elif opcionUsuario == 3:
    
else:
    print("\nSALIR")