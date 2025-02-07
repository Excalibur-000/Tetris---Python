import pygame
from settings import *

class Game:
    def __init__(self, screen):
        # Define screen
        self.screen = screen

        # Create a sprite group
        self.camera_group = pygame.sprite.Group()

        # Render background image
        self.background = pygame.image.load('Tetris - Python/assets/Visual/grid.png').convert()
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # Create text/fonts
        self.tetris_font = pygame.font.Font('Tetris - Python/assets/Fonts/Roboto-VariableFont_wdth,wght.ttf', 32)
        self.tetris_text = self.tetris_font.render('Tetris', True, (255, 255, 255))
        self.title_pos = self.tetris_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 19))

        # Create a display surface
        self.display_surface_width = DISPLAY_WIDTH 
        self.display_surface_height = DISPLAY_HEIGHT
        self.display_surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.display_surface.fill(FG_COLOUR)
        self.display_surface_pos = self.display_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.83))

    def run(self, dt):
        # Update camera group
        self.camera_group.update(dt)

        # Draws background
        self.screen.blit(self.background, self.background.get_rect())

        # Draws title and display surface
        self.screen.blit(self.tetris_text, self.title_pos)
        self.screen.blit(self.display_surface, self.display_surface_pos)