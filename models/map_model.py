import pygame
import os


class MapModel:
    def __init__(self, ancho_pantalla=800, alto_pantalla=600):
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla
        self.scroll_x = 0  # Posición actual de la cámara

        # Límites máximos del scroll (como tenemos 3 pantallas de 800px de ancho)
        self.ancho_total_mapa = ancho_pantalla * 3
        self.max_scroll = self.ancho_total_mapa - ancho_pantalla

        # Cargar las tres imágenes de los escenarios
        ruta_base = os.path.join("assets", "images")

        try:
            self.imagen_1 = pygame.image.load(
                os.path.join(ruta_base, "pantalla1.jpg")
            ).convert()
            self.imagen_2 = pygame.image.load(
                os.path.join(ruta_base, "pantalla2.jpg")
            ).convert()
            self.imagen_3 = pygame.image.load(
                os.path.join(ruta_base, "pantalla3.jpg")
            ).convert()

            # Asegurarnos de que las imágenes tienen el tamaño de la pantalla
            self.imagen_1 = pygame.transform.scale(
                self.imagen_1, (ancho_pantalla, alto_pantalla)
            )
            self.imagen_2 = pygame.transform.scale(
                self.imagen_2, (ancho_pantalla, alto_pantalla)
            )
            self.imagen_3 = pygame.transform.scale(
                self.imagen_3, (ancho_pantalla, alto_pantalla)
            )
        except Exception as e:
            print(f"Error al cargar las imágenes: {e}")
            print(
                "Asegúrate de que pantalla1.jpg, pantalla2.jpg y pantalla3.jpg están en la carpeta assets/images/"
            )

    def mover_derecha(self, velocidad=5):
        """Mueve la cámara hacia la derecha sin pasarse del final del mapa"""
        self.scroll_x += velocidad
        if self.scroll_x > self.max_scroll:
            self.scroll_x = self.max_scroll

    def mover_izquierda(self, velocidad=5):
        """Mueve la cámara hacia la izquierda sin pasarse del inicio"""
        self.scroll_x -= velocidad
        if self.scroll_x < 0:
            self.scroll_x = 0
