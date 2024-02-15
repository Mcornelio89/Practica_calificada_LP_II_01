class Forma:
    def dibujar(self):
        print("Dibujando forma")

class Color:
    def __init__(self, color):
        self.color = color

    def pintar(self):
        print(f"Pintando con {self.color}")

class CuadradoColorido(Forma, Color):
    def forma_y_color(self):
        super().dibujar()
        print("Cuadrado")
        super().pintar()

# Crear instancia de CuadradoColorido
cuadrado_colorido = CuadradoColorido("Rojo")

cuadrado_colorido.forma_y_color()