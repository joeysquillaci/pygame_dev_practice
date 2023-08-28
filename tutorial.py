# Import necessary libraries
import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):

        # Initiate pygame
        pygame.init()
        # Name the pygame window
        pygame.display.set_caption('Pygame Development')

        # Set screen size
        self.screen = pygame.display.set_mode((640, 480))
        # Instantiate a clock object
        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))



    def run(self):
        while True:

            # Fill the screen with a light blue color
            self.screen.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))   
            self.player.render(self.screen)    


            # Check for user input
            for event in pygame.event.get():
                # Check if user wants to exit program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Check if key is pressed down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                # Check if key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                        

            # Update the display
            pygame.display.update()
            # Set FPS
            self.clock.tick(60)

# Run the game
Game().run()

