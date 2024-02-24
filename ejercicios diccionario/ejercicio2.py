import re

class ContadorPalabras:
    def __init__(self):
        # Inicializar un diccionario vacío para contar las palabras
        self.contador = {}

    def contar_apariciones(self, texto):
        # Utilizar expresiones regulares para dividir el texto en palabras
        palabras = re.findall(r'\b\w+\b', texto.lower())

        # Contar la aparición de cada palabra
        for palabra in palabras:
            if palabra in self.contador:
                self.contador[palabra] += 1
            else:
                self.contador[palabra] = 1

    def obtener_resultados(self):
        # Devolver el diccionario con las apariciones de cada palabra
        return self.contador

# Ejemplo de uso
contador = ContadorPalabras()

texto_ejemplo = "Este es un ejemplo de texto. Este texto contiene palabras, y algunas palabras se repiten en el texto."

contador.contar_apariciones(texto_ejemplo)

resultados = contador.obtener_resultados()
print("Apariciones de cada palabra:")
for palabra, apariciones in resultados.items():
    print(f"{palabra}: {apariciones}")