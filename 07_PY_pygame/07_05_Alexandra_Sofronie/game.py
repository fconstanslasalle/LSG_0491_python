import pygame
import random

# Inicializa pygame
pygame.init()

# Configuración de la pantalla
ANCHO_PANTALLA = 600
ALTO_PANTALLA = 400
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Breakout")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)

# Cargar las imágenes de los bloques
bloque_rojo = pygame.image.load('img/bloques/bloqueRojo.png')
bloque_azul = pygame.image.load('img/bloques/bloqueAzul.png')
bloque_verde = pygame.image.load('img/bloques/bloqueVerde.png')
bloque_amarillo = pygame.image.load('img/bloques/bloqueAmarillo.png')
bloque_lila = pygame.image.load('img/bloques/bloqueLila.png')
bloque_gris = pygame.image.load('img/bloques/bloqueGris.png')
imagenes_bloques = [bloque_rojo, bloque_azul, bloque_verde, bloque_amarillo, bloque_lila, bloque_gris]

# Cargar las imágenes de la paleta
paleta_rojo = pygame.image.load('img/barras/barraRoja.png')
paleta_azul = pygame.image.load('img/barras/barraAzul.png')
paleta_verde = pygame.image.load('img/barras/barraVerde.png')
paleta_amarillo = pygame.image.load('img/barras/barraAmarilla.png')
paleta_lila = pygame.image.load('img/barras/barraLila.png')
paleta_gris = pygame.image.load('img/barras/barraGris.png')
imagenes_paleta = [paleta_rojo, paleta_azul, paleta_verde, paleta_amarillo, paleta_lila, paleta_gris]

# Cargar las imágenes de la pelota
bola_rojo = pygame.image.load('img/bola/bolaRoja.png')
bola_azul = pygame.image.load('img/bola/bolaAzul.png')
bola_verde = pygame.image.load('img/bola/bolaVerde.png')
bola_amarillo = pygame.image.load('img/bola/bolaAmarilla.png')
bola_lila = pygame.image.load('img/bola/bolaLila.png')
bola_gris = pygame.image.load('img/bola/bolaGris.png')
imagenes_bola = [bola_rojo, bola_azul, bola_verde, bola_amarillo, bola_lila, bola_gris]

# Fuente
fuente = pygame.font.Font(None, 36)

# Configuración de la paleta y pelota
class Paleta:
    def __init__(self, x, y, ancho, alto, velocidad, imagen):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.velocidad = velocidad
        self.imagen = imagen

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.x < ANCHO_PANTALLA - self.rect.width:
            self.rect.x += self.velocidad

    def dibujar(self):
        pantalla.blit(self.imagen, self.rect)
class Pelota:
    def __init__(self, x, y, radio, velocidad_inicial, imagen):
        self.rect = pygame.Rect(x - radio, y - radio, radio * 2, radio * 2)
        self.velocidad_x = velocidad_inicial * random.choice([-1, 1])
        self.velocidad_y = -velocidad_inicial
        self.radio = radio
        self.imagen = pygame.transform.scale(imagen, (radio * 2, radio * 2))  # Escalar imagen de la bola

    def mover(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

    def dibujar(self):
        pantalla.blit(self.imagen, self.rect)

    def mover(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

    def colision_bordes(self):
        if self.rect.x <= 0 or self.rect.x >= ANCHO_PANTALLA - self.rect.width:
            self.velocidad_x *= -1
        if self.rect.y <= 0:
            self.velocidad_y *= -1

    def colision_paleta(self, paleta):
        if self.rect.colliderect(paleta.rect):
            self.velocidad_y *= -1

    def dibujar(self):
        pantalla.blit(self.imagen, self.rect)

class Bloque:
    def __init__(self, x, y, ancho, alto, imagen):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.imagen = imagen

# Función para mostrar los mensajes
def mostrar_mensaje(titulo, subtitulo, color_titulo, color_subtitulo):
    activo = True
    while activo:
        pantalla.fill(NEGRO)
        titulo_texto = fuente.render(titulo, True, color_titulo)
        subtitulo_texto = fuente.render(subtitulo, True, color_subtitulo)
        pantalla.blit(titulo_texto, ((ANCHO_PANTALLA - titulo_texto.get_width()) // 2, 100))
        pantalla.blit(subtitulo_texto, ((ANCHO_PANTALLA - subtitulo_texto.get_width()) // 2, 200))
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:  # Continuar juego
                    activo = False
                if evento.key == pygame.K_ESCAPE:  # Salir del juego
                    pygame.quit()
                    exit()

# Función para reiniciar el juego
def reiniciar_juego(nivel=1):
    global puntaje, bloques, filas
    imagen_paleta = random.choice(imagenes_paleta)  # Selecciona una imagen aleatoria para la paleta
    paleta = Paleta((ANCHO_PANTALLA - 80) // 2, ALTO_PANTALLA - 30, 80, 10, 10, imagen_paleta)
    imagen_bola = random.choice(imagenes_bola)  # Selecciona una imagen aleatoria para la bola
    pelota = Pelota(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2, 9, 4, imagen_bola)
    bloques = []
    filas = 5 + nivel - 1

    # Generar bloques
    for fila in range(filas):
        for col in range(10):
            bloque_x = col * (50 + 5) + 35
            bloque_y = fila * (20 + 5) + 80
            imagen = random.choice(imagenes_bloques)
            bloques.append(Bloque(bloque_x, bloque_y, 50, 20, imagen))

    puntaje = 0 if nivel == 1 else puntaje
    return paleta, pelota, bloques

# Inicializar el juego
nivel = 1
puntaje = 0
paleta, pelota, bloques = reiniciar_juego(nivel)
mostrar_mensaje("BREAKOUT", "Presiona ESPACIO para jugar", BLANCO, BLANCO)

# Bucle principal del juego
ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    pantalla.fill(NEGRO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    paleta.mover()
    pelota.mover()

    pelota.colision_bordes()
    pelota.colision_paleta(paleta)

    bloques_rotos = []
    for i, bloque in enumerate(bloques):
        if pelota.rect.colliderect(bloque.rect):
            pelota.velocidad_y *= -1
            bloques_rotos.append(i)
            puntaje += 10

    for i in sorted(bloques_rotos, reverse=True):
        del bloques[i]

    if not bloques:
        mostrar_mensaje("YOU WIN!", "Presiona ESPACIO para el siguiente nivel", AZUL, BLANCO)
        nivel += 1
        paleta, pelota, bloques = reiniciar_juego(nivel)

    if pelota.rect.y >= ALTO_PANTALLA:
        mostrar_mensaje("GAME OVER", "Presiona ESPACIO para jugar de nuevo", ROJO, BLANCO)
        nivel = 1
        paleta, pelota, bloques = reiniciar_juego(nivel)

    for bloque in bloques:
        pantalla.blit(bloque.imagen, bloque.rect)
    paleta.dibujar()
    pelota.dibujar()

    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    texto_nivel = fuente.render(f"Nivel: {nivel}", True, BLANCO)
    pantalla.blit(texto_puntaje, (10, 5))
    pantalla.blit(texto_nivel, (10, 40))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
