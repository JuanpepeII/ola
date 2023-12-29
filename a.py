import random
import time

WIDTH = 1024
HEIGHT = 576

# Musica
music.set_volume(.03)
music.play('rararainbowmuffin')

# Variables
points = 0 # Esta variable definirá la cantidad de respuestas correctas que tiene el jugador
level = 0 # Esta variable definirá el nivel que se encuentra el jugador, servirá para dibujar el nivel correspondiente en la función draw()
cd = 1 # Variable puesta para el cooldown de seleccion de respuestas, mas informacion en las funciones correspondientes

# Assets
BOX = Rect((192, 30), (640, 120)) # Cajas donde se colocara texto con preguntas o respuestas
BOX2 = Rect((252, 180), (520, 100))
BOX3 = Rect((252, 300), (520, 100))
BOX4 = Rect((252, 420), (520, 100))
BoxOutline = Rect((182, 20), (660, 140)) # Estas cajas simularan un borde, ya que estaran dibujadas por detras
BoxOutline2 = Rect((242, 170), (540, 120))
BoxOutline3 = Rect((242, 290), (540, 120))
BoxOutline4 = Rect((242, 410), (540, 120))

# Diseño de niveles
def draw(): # El valor de level en cada if define el nivel que esta dibujando, a excepción del level == 0, -1 y 9
    global level
    if level == 0: # Menú
        screen.fill((255, 249, 249)) # Color del fondo
        screen.draw.filled_rect(BoxOutline, "black") # Esta caja se coloca por detras de la caja blanca para simular un borde
        screen.draw.filled_rect(BOX, "white") # Cuadrado blanco que portará el titulo del juego
        screen.draw.textbox("Mega quiz matematico", BOX, color="black") # Texto que irá en el cuadro

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("Jugar", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("Salir", BOX3, color="black")

        screen.draw.text("Hecho por: \nMauricio Rivera \nSamantha Neira", (2, 521), color="black") # Nombres de los integrantes, puestos en la esquina inferior izquierda
        screen.draw.text("Todos los derechos reservados ©", (745, 556), color="black") # Copyright, inferior derecha

    if level == -1:
        print("Hola mundo")
        si += 1 # Crashea el juego a proposito para salir.

    if level == 1:
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white") # En esta caja, irá la pregunta, lo mismo con los demás nivelesa
        screen.draw.textbox("El numero que esta arriba de una fraccion se llama...", BOX, color="black") # Texto dentro de la caj

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("Numerador", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("Denominador", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("Juan", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black") # Muestra la cantidad de respuestas correctas al borde inferior izquierda

    if level == 2:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Si el lado de un cuadrado es 9cm ¿Cuanto mide su area?", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("18cm²", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("24cm²", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("81cm²", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black")

    if level == 3:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Si un dulce vale $330 ¿cuantos dulces puedo comprar con $1200?", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("4 dulces", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("5 dulces", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("3 dulces", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black")

    if level == 4:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Resuelve la ecuacion \n2x + 4 = 72", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("x = 32", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("x = 34", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("x = 39", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black")

    if level == 5:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Es la suma iterada de un numero", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("Division", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("Potencia", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("Multiplicacion", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black")

    if level == 6:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Nombre del angulo que mide 90°", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("Agudo", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("Recto", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("Extendido", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black")

    if level == 7:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Cual es el unico numero primo par?", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("2", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("4", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("6", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black")

    if level == 8:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Cuantos segundos hay en un dia?", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox("100,000 segundos", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("12,500 segundos", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("86,400 segundos", BOX4, color="black")

        screen.draw.text(f"Respuestas correctas: {points}", (2, 556), color="black")

    if level == 9:
        screen.clear()
        screen.fill((255, 249, 249))
        screen.draw.filled_rect(BoxOutline, "black")
        screen.draw.filled_rect(BOX, "white")
        screen.draw.textbox("Felicidades! Estos fueron tus resultados", BOX, color="black")

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, "white")
        screen.draw.textbox(f"{points}/8 respuestas correctas!", BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, "white")
        screen.draw.textbox("Muchas gracias por jugar", BOX3, color="black")

        screen.draw.filled_rect(BoxOutline4, "black")
        screen.draw.filled_rect(BOX4, "white")
        screen.draw.textbox("Salir", BOX4, color="black")


def update():
    global level #El unico proposito de este update lograr que cargue correctamente el juego, ya que de otra manera se ven botdes negros


def on_mouse_down(pos):  # Interacciones con los botones en pantalla
    # Variables globales
    global level
    global cd
    global points

    if BOX2.collidepoint(pos):  # Interacciones con primer cuadro,
        if cd == 1 and level < 9:
            cd = 0 # Cambia el valor de cd para que no pase lo explicado en la función cooldown()
            if level == 1 or level == 3 or level == 7: # El primer cuadro será la respuesta correcta de la pregunta 1, 3 y 7
                points += 1
                print("Respuesta correcta!\n")
            elif level > 0: # De no estar en los niveles 1, 3 o 7, si se apreta esta caja, mostrará el mensaje de respuesta incorrecta
                print("Respuesta incorrecta!\n")
            level += 1
            print(f"Nivel {level}")
            clock.schedule_unique(cooldown, 0.1) # Llama a la función cooldown() despues de un pequeño lapso para poder volver a clickear la siguiente respuesta

    if BOX3.collidepoint(pos):
        if cd == 1 and level < 9:
            cd = 0
            if level == 4 or level == 6: # El segundo cuadro será la respuesta correcta de la pregunta 4 y 6
                points += 1
                print("Respuesta correcta!\n")
            elif level == 0: # Boton salir del menú
                level += -2
            elif level > 0: # De no estar en los niveles 4 o 6, si se apreta esta caja, mostrará el mensaje de respuesta incorrecta
                print("Respuesta incorrecta!\n")
            level += 1
            print(f"Nivel {level}")
            clock.schedule_unique(cooldown, 0.1)

    if BOX4.collidepoint(pos):
        if cd == 1 and level > 0:
            cd = 0
            if level == 2 or level == 5 or level == 8: # El tercer cuadro será la respuesta correcta de la pregunta 2, 5 y 8
                points += 1
                print("Respuesta correcta!\n")
            elif level == 9: # Boton salir pantalla final
                level = -2
            elif level > 0: # De no estar en los niveles 2, 5 u 8, si se apreta esta caja, mostrará el mensaje de respuesta incorrecta
                print("Respuesta incorrecta!\n")
            level += 1
            print(f"Nivel {level}")
            clock.schedule_unique(cooldown, 0.1)


def cooldown(): # Función de cooldown de interacciones, agregado ya que sin esto al mantener presionado el mouse
    global cd    # para seleccionar una respuesta, se pasarian varios niveles al mismo tiempo
    cd = 1        # Con esto se puede mantener pulsado el click y no pasara de nivel hasta que se vuelva a presionar
