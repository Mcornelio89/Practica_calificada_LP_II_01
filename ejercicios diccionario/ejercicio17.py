class GestorRecetas:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar las recetas
        self.recetas = {}

    def agregar_receta(self, nombre_receta, ingredientes, pasos):
        # Agregar una receta al diccionario
        if nombre_receta not in self.recetas:
            self.recetas[nombre_receta] = {'ingredientes': ingredientes, 'pasos': pasos}
            print(f"Receta '{nombre_receta}' agregada.")
        else:
            print(f"La receta '{nombre_receta}' ya existe.")

    def obtener_receta(self, nombre_receta):
        # Obtener la información de una receta por su nombre
        return self.recetas.get(nombre_receta, None)

    def obtener_todas_las_recetas(self):
        # Devolver todas las recetas y su información
        return self.recetas

# Ejemplo de uso
gestor_recetas = GestorRecetas()

# Agregar recetas al diccionario
gestor_recetas.agregar_receta('Tarta de Manzana', ['manzanas', 'azúcar', 'harina'], ['Paso 1: Pelar y cortar las manzanas', 'Paso 2: Mezclar con azúcar y harina', 'Paso 3: Hornear'])

gestor_recetas.agregar_receta('Ensalada César', ['lechuga', 'pollo', 'crutones'], ['Paso 1: Cortar la lechuga', 'Paso 2: Cocinar el pollo', 'Paso 3: Mezclar con crutones'])

# Obtener información de una receta
info_tarta_manzana = gestor_recetas.obtener_receta('Tarta de Manzana')
print("Información de la Tarta de Manzana:", info_tarta_manzana)

# Obtener todas las recetas y su información
todas_las_recetas = gestor_recetas.obtener_todas_las_recetas()
print("Todas las recetas:", todas_las_recetas)