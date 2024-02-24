class AnalizadorRedesSociales:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar información de los usuarios y sus seguidores
        self.usuarios = {}

    def agregar_usuario(self, nombre_usuario, seguidores):
        # Agregar un usuario al diccionario
        self.usuarios[nombre_usuario] = {'seguidores': seguidores}

    def obtener_seguidores(self, nombre_usuario):
        # Obtener el número de seguidores de un usuario
        usuario = self.usuarios.get(nombre_usuario, None)
        if usuario:
            return usuario['seguidores']
        else:
            print(f"No se encontró información para el usuario {nombre_usuario}.")
            return None

    def actualizar_seguidores(self, nombre_usuario, nuevos_seguidores):
        # Actualizar el número de seguidores de un usuario
        usuario = self.usuarios.get(nombre_usuario, None)
        if usuario:
            usuario['seguidores'] = nuevos_seguidores
        else:
            print(f"No se encontró información para el usuario {nombre_usuario}.")

    def eliminar_usuario(self, nombre_usuario):
        # Eliminar un usuario del diccionario
        if nombre_usuario in self.usuarios:
            del self.usuarios[nombre_usuario]
        else:
            print(f"No se encontró información para el usuario {nombre_usuario}.")

    def obtener_todos_los_usuarios(self):
        # Devolver todos los usuarios y sus seguidores en el diccionario
        return self.usuarios

# Ejemplo de uso
analizador_redes = AnalizadorRedesSociales()

# Agregar usuarios al diccionario
analizador_redes.agregar_usuario('Juan', 1000)
analizador_redes.agregar_usuario('María', 800)

# Obtener el número de seguidores de un usuario
seguidores_juan = analizador_redes.obtener_seguidores('Juan')
print("Seguidores de Juan:", seguidores_juan)

# Actualizar el número de seguidores de un usuario
analizador_redes.actualizar_seguidores('Juan', 1200)

# Eliminar un usuario del diccionario
analizador_redes.eliminar_usuario('María')

# Obtener todos los usuarios y sus seguidores
todos_los_usuarios = analizador_redes.obtener_todos_los_usuarios()
print("Todos los usuarios y sus seguidores:", todos_los_usuarios)