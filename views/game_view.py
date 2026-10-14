import pygame

class GameView:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def dibujar(self, modelo):
        # Limpiar la pantalla por si acaso
        self.pantalla.fill((0, 0, 0))
        
        # Obtener el desplazamiento actual de la cámara
        scroll_x = modelo.scroll_x
        
        # Dibujar las tres pantallas en fila horizontal restando el scroll
        self.pantalla.blit(modelo.imagen_1, (-scroll_x, 0))
        self.pantalla.blit(modelo.imagen_2, (modelo.ancho_pantalla - scroll_x, 0))
        self.pantalla.blit(modelo.imagen_3, (modelo.ancho_pantalla * 2 - scroll_x, 0))