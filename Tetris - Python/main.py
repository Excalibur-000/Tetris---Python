import pygame
import sys
from settings import *
from game import *

class Main:
    def __init__(self):
        # Initialise pygame
        pygame.init()

        # Start clock for delta time
        self.clock = pygame.time.Clock()

        # Define screen and fills it
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Creates game object
        self.game = Game(self.screen)

    def game_loop(self):        
        # Loops through events and executes the appropriate action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        # Main loop
        while True:
            dt = self.clock.tick() / 1000
            self.screen.fill(BG_COLOUR) 
            self.game_loop()
            self.game.run(dt)
            pygame.display.update()  

if __name__ == '__main__':
    main = Main()
    main.run()



            