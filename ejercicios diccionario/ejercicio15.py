class SistemaVotaciones:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar los votos de cada candidato
        self.votos = {}

    def agregar_voto(self, candidato):
        # Agregar un voto al diccionario
        if candidato not in self.votos:
            self.votos[candidato] = 1
        else:
            self.votos[candidato] += 1

    def obtener_votos(self, candidato):
        # Obtener la cantidad de votos de un candidato
        return self.votos.get(candidato, 0)

    def obtener_todos_los_votos(self):
        # Devolver todos los votos de cada candidato en el diccionario
        return self.votos

# Ejemplo de uso
sistema_votaciones = SistemaVotaciones()

# Agregar votos al diccionario
sistema_votaciones.agregar_voto('Candidato A')
sistema_votaciones.agregar_voto('Candidato B')
sistema_votaciones.agregar_voto('Candidato A')
sistema_votaciones.agregar_voto('Candidato C')

# Obtener la cantidad de votos de un candidato
votos_candidato_a = sistema_votaciones.obtener_votos('Candidato A')
print("Votos del Candidato A:", votos_candidato_a)

# Obtener todos los votos de cada candidato
todos_los_votos = sistema_votaciones.obtener_todos_los_votos()
print("Todos los votos:", todos_los_votos)