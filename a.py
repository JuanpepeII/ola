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
color_original = (255, 255, 255) # Blanco
color_hover = (230, 230, 230) # Gris
color_bien = (48, 255, 36) # Verde
color_mal = (254, 32, 32) # Rojo

# Colores de las cajas de respuestas
color1 = color_original
color2 = color_original
color3 = color_original


# listas que contendran las preguntas y respuestas
preguntas = ["Mega quiz matematico", "Como se llama el numero ubicado arriba de una fraccion?", "Si el lado de un cuadrado es 9cm ¿Cuanto mide su area?", "Si un dulce vale $330 ¿cuantos dulces puedo comprar con $1200?", "Resuelve la ecuacion \n2x + 4 = 72", "Es la suma iterada de un numero", "Nombre del angulo que mide 90°", "Cual es el unico numero primo par?", "Cuantos segundos hay en un dia?", "Felicidades! Estos fueron tus resultados"]
respuestas1 = ["Jugar", "Numerador", "18cm", "3 dulces", "x = 32", "Division", "Agudo", "2", "100,000 segundos", " "]
respuestas2 = ["Salir", "Denominador", "24cm", "5 dulces", "x = 34", "Potencia", "Recto", "4", "12,500 segundos", "Muchas gracias por jugar"]
respuestas3 = ["", "Juan", "81cm", "4 dulces", "x = 39", "Multiplicacion", "Extendido", "6", "86,400 segundos", "Salir"]

# Cajas donde se colocara texto con preguntas o respuestas
BOX = Rect((192, 30), (640, 120)) 
BOX2 = Rect((252, 180), (520, 100))
BOX3 = Rect((252, 300), (520, 100))
BOX4 = Rect((252, 420), (520, 100))
# Estas cajas simularan un borde, ya que estaran dibujadas por detras
BoxOutline = Rect((182, 20), (660, 140)) 
BoxOutline2 = Rect((242, 170), (540, 120))
BoxOutline3 = Rect((242, 290), (540, 120))
BoxOutline4 = Rect((242, 410), (540, 120))

# Diseño de niveles
def draw(): # El valor de level en cada if define el nivel que esta dibujando, a excepción del level == 0, -1 y 9
    global level
    global preguntas
    global respuestas2
    global respuestas1
    global respuestas3
    if level < 10: # Menú y niveles
        screen.fill((255, 249, 249)) # Color del fondo
        screen.draw.filled_rect(BoxOutline, "black") # Esta caja se coloca por detras de la caja blanca para simular un borde
        screen.draw.filled_rect(BOX, "white") # Cuadrado blanco que portará el titulo del juego
        screen.draw.textbox(preguntas[level], BOX, color="black") # Texto que irá en el cuadro

        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, color1)
        screen.draw.textbox(respuestas1[level], BOX2, color="black")

        screen.draw.filled_rect(BoxOutline3, "black")
        screen.draw.filled_rect(BOX3, color2)
        screen.draw.textbox(respuestas2[level], BOX3, color="black")
        
        if level > 0:
            screen.draw.filled_rect(BoxOutline4, "black")
            screen.draw.filled_rect(BOX4, color3)
            screen.draw.textbox(respuestas3[level], BOX4, color="black")

        screen.draw.text("Hecho por: \nMauricio Rivera \nSamantha Neira", (2, 521), color="black") # texto inferior izquierda
        screen.draw.text("Todos los derechos reservados ©", (745, 556), color="black") # Copyright, inferior derecha
        
    if level == 9: # Se dibuja otro cuadro aparte en la pantalla final, ya que no se actualiza el numero de respuestas correctas dentro de la lista
        screen.draw.filled_rect(BoxOutline2, "black")
        screen.draw.filled_rect(BOX2, color1)
        screen.draw.textbox(f"{points}/8 respuestas correctas!", BOX2, color="black")



def update():
    global level #El unico proposito de este update lograr que cargue correctamente el juego, ya que de otra manera se ven botdes negros


def on_mouse_down(pos):  # Interacciones con los botones en pantalla
    # Variables globales
    global level
    global cd
    global points
    global color1
    global color2
    global color3
    global color_original
    global color_bien
    global color_mal

    if BOX2.collidepoint(pos):  # Interacciones con primer cuadro,
        if cd == 1 and level < 9:
            cd = 0 # Cambia el valor de cd para que no pase lo explicado en la función cooldown()
            if level == 1 or level == 3 or level == 7: # El primer cuadro será la respuesta correcta de la pregunta 1, 3 y 7 y el cuadro se volvera verde
                points += 1
                print("Respuesta correcta!\n")
                color1 = color_bien
            elif level > 0: # De no estar en los niveles 1, 3 o 7, si se apreta esta caja, mostrará el mensaje de respuesta incorrecta y el cuadro se volvera rojo
                print("Respuesta incorrecta!\n")
                color1 = color_mal
            clock.schedule_unique(siguiente_nivel, 1) # Llama a la función siguiente_nivel() para pasar de nivel despues de un segundo
            clock.schedule_unique(cooldown, 1) # Llama a la función cooldown() despues de un pequeño lapso para poder volver a clickear la siguiente respuesta

    if BOX3.collidepoint(pos):
        if cd == 1 and level < 9:
            cd = 0
            if level == 4 or level == 6: # El segundo cuadro será la respuesta correcta de la pregunta 4 y 6 y el cuadro se volvera verde
                points += 1
                print("Respuesta correcta!\n")
                color2 = color_bien
            elif level == 0: # Boton salir del menú, se crashea el juego a proposito
                si += 1
            elif level > 0: # De no estar en los niveles 4 o 6, si se apreta esta caja, mostrará el mensaje de respuesta incorrecta y el cuadro se volvera rojo
                print("Respuesta incorrecta!\n")
                color2 = color_mal
            clock.schedule_unique(siguiente_nivel, 1)
            clock.schedule_unique(cooldown, 1)

    if BOX4.collidepoint(pos):
        if cd == 1 and level > 0:
            cd = 0
            if level == 2 or level == 5 or level == 8: # El tercer cuadro será la respuesta correcta de la pregunta 2, 5 y 8 y el cuadro se volvera verde
                points += 1
                print("Respuesta correcta!\n")
                color3 = color_bien
            elif level == 9: # Boton salir pantalla final, se crashea el juego a proposito
                si += 1
            elif level > 0: # De no estar en los niveles 2, 5 u 8, si se apreta esta caja, mostrará el mensaje de respuesta incorrecta y el cuadro se volvera rojo
                print("Respuesta incorrecta!\n")
                color3 = color_mal
            clock.schedule_unique(siguiente_nivel, 1)
            clock.schedule_unique(cooldown, 1)

def on_mouse_move(pos): # Esta función hace que al pasar el mouse por encima de un botón, este se vuelva gris
    global cd
    global color1
    global color2
    global color3
    global color_original
    global color_hover
    
    if BOX2.collidepoint(pos) and cd == 1:
        color1 = color_hover
    elif cd == 1:
        color1 = color_original

    if BOX3.collidepoint(pos) and cd == 1:
        color2 = color_hover
    elif cd == 1:
        color2 = color_original
    
    if BOX4.collidepoint(pos) and cd == 1:
        color3 = color_hover
    elif cd == 1:
        color3 = color_original


def siguiente_nivel():
    global level
    global color1
    global color2
    global color3
    global color_original
    
    level += 1
    print(f"Nivel {level}")
    
    # El cambio de color aqui se asegura que inmediatamente al cambiar de nivel, se cambia al color original, de otra manera de quedara de color verde o rojo hasta mover el mouse
    color1 = color_original
    color2 = color_original
    color3 = color_original

def cooldown(): # Función de cooldown de interacciones, agregado ya que sin esto al mantener presionado el mouse
    global cd    # para seleccionar una respuesta, se pasarian varios niveles al mismo tiempo
    cd = 1        # Con esto se puede mantener pulsado el click y no pasara de nivel hasta que se vuelva a presionar
