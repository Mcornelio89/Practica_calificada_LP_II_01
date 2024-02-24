class BibliotecaPersonal:
    def __init__(self):
        # Inicializar una lista vacía para almacenar los libros
        self.libros = []

    def agregar_libro(self, titulo, autor, año):
        # Agregar un libro a la biblioteca
        libro = {'titulo': titulo, 'autor': autor, 'año': año}
        self.libros.append(libro)

    def buscar_libro_por_titulo(self, titulo):
        # Buscar un libro por su título en la biblioteca
        for libro in self.libros:
            if libro['titulo'] == titulo:
                return libro
        return None

    def buscar_libros_por_autor(self, autor):
        # Buscar libros por autor en la biblioteca
        libros_autor = []
        for libro in self.libros:
            if libro['autor'] == autor:
                libros_autor.append(libro)
        return libros_autor

    def buscar_libros_por_año(self, año):
        # Buscar libros por año en la biblioteca
        libros_año = []
        for libro in self.libros:
            if libro['año'] == año:
                libros_año.append(libro)
        return libros_año

    def obtener_todos_los_libros(self):
        # Devolver todos los libros en la biblioteca
        return self.libros

# Ejemplo de uso
mi_biblioteca = BibliotecaPersonal()

# Agregar libros a la biblioteca
mi_biblioteca.agregar_libro('El señor de los anillos', 'J.R.R. Tolkien', 1954)
mi_biblioteca.agregar_libro('1984', 'George Orwell', 1949)
mi_biblioteca.agregar_libro('Cien años de soledad', 'Gabriel García Márquez', 1967)

# Buscar un libro por título
libro_1984 = mi_biblioteca.buscar_libro_por_titulo('1984')
print("Información del libro '1984':", libro_1984)

# Buscar libros por autor
libros_tolkien = mi_biblioteca.buscar_libros_por_autor('J.R.R. Tolkien')
print("Libros de J.R.R. Tolkien:", libros_tolkien)

# Obtener todos los libros en la biblioteca
todos_los_libros = mi_biblioteca.obtener_todos_los_libros()
print("Todos los libros en la biblioteca:", todos_los_libros)