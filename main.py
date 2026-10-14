import pygame
import sys
from models.map_model import MapModel
from views.game_view import GameView

def main():
    pygame.init()
    
    # Configurar la ventana
    ANCHO, ALTO = 800, 600
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mi Juego con Scroll Horizontal")
    
    reloj = pygame.time.Clock()

    # Inicializar Modelo y Vista
    modelo = MapModel(ANCHO, ALTO)
    vista = GameView(pantalla)

    # Bucle principal del juego
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Capturar teclas presionadas continuamente (ej. flechas para moverse)
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT]:
            modelo.mover_derecha(velocidad=6)
        if teclas[pygame.K_LEFT]:
            modelo.mover_izquierda(velocidad=6)

        # Dibujar los escenarios según la posición de la cámara
        vista.dibujar(modelo)
        
        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()