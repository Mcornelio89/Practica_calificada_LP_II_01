import random

def juego_adivinar_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_a_adivinar = random.randint(1, 100)
    
    # Inicializar variables
    intentos_realizados = 0
    max_intentos = 10  # Puedes ajustar este límite según tus preferencias
    
    print("¡Bienvenido al juego de adivinar el número!")
    print(f"Adivina un número entre 1 y 100. Tienes un máximo de {max_intentos} intentos.")

    while intentos_realizados < max_intentos:
        # Pedir al usuario que ingrese un número
        intento_usuario = int(input("Ingresa tu intento: "))
        
        # Contar el intento
        intentos_realizados += 1
        
        # Verificar si el número es igual al número a adivinar
        if intento_usuario == numero_a_adivinar:
            print(f"¡Felicidades! Has adivinado el número {numero_a_adivinar} en {intentos_realizados} intentos.")
            break
        elif intento_usuario < numero_a_adivinar:
            print("El número es mayor. ¡Sigue intentando!")
        else:
            print("El número es menor. ¡Sigue intentando!")

    # Si el usuario no adivina dentro del límite de intentos
    if intentos_realizados == max_intentos:
        print(f"¡Lo siento! Has alcanzado el límite de intentos. El número correcto era {numero_a_adivinar}.")

# Llamar a la función para iniciar el juego
juego_adivinar_numero()