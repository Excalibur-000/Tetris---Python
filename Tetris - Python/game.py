import pygame
from settings import *

class Game:
    def __init__(self, screen):
        # Define screen
        self.screen = screen

        # Create a sprite group
        self.camera_group = pygame.sprite.Group()

        # Create text/fonts
        self.tetris_font = pygame.font.Font(None, 40)
        self.tetris_text = self.tetris_font.render('Tetris', True, (255, 255, 255))
        self.title_pos = self.tetris_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20))

        self.line_font = pygame.font.Font(None, 30)
        self.line = self.line_font.render(('_'*100), True, (255, 255, 255))
        self.line_pos = self.line.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 15))

        # Create a purple display surface
        self.display_surface_width = DISPLAY_WIDTH 
        self.display_surface_height = DISPLAY_HEIGHT
        self.display_surface = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.display_surface.fill(FG_COLOUR)
        self.display_surface_pos = self.display_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.84))

    def run(self, dt):
        # Update camera group
        self.camera_group.update(dt)

        # Draws title, line and display surface
        self.screen.blit(self.tetris_text, self.title_pos)
        self.screen.blit(self.line, self.line_pos)
        self.screen.blit(self.display_surface, self.display_surface_pos)