#1.Añadir empleado
#2.Eliminar empleado
#3.Mostrar todos los empleados
#4.Salir

print("\n1.Añadir empleado.\n2.Eliminar empleado.\n3.Mostrar todos los empleados.\n4.Salir")
opcionUsuario = int(input("Opción   :   "))

listaEmpleado = []

if opcionUsuario == 1:
    cantidadEmpleados = int(input("Ingrese la cantidad de empleados:"))
while cantidadEmpleados < 0:
    cantidadEmpleados = int(input("Ingrese la cantidad de empleados:"))
for i in range (cantidadEmpleados):
    print ("Empleado #", i +1)
    IDempelado = input ("Ingrese el IDempleado:")
    nombre = input ("Ingrese el nombre del empleado:")
    departamento = input("Ingrese el departamento:")
    salario = float (input("Ingrese el salario:"))
    while salario <= 0:
        print("!!El salario no puede ser negativo!!")
        salario = float (input("Ingrese el salario:"))
    listaEmpleados.append([IDempleado,nombre,departamento,salario])
    print ("Empleado registrado")
print ("lista de Empleados y salario:")
for empleado in listaEmpelados:
    print (f"IDempleado: {empleado[0]} - nombre: {empleado [1]} - departamento: {empleado [2]} - salario: {empleado [3]} ")
elif opcionUsuario == 2:
    
elif opcionUsuario == 3:
    
else:
    print("\nSALIR")