# Import necessary libraries
import pygame
import sys


class Game:
    def __init__(self):

        # Initiate pygame
        pygame.init()
        # Name the pygame window
        pygame.display.set_caption('Pygame Development')

        # Set screen size
        self.screen = pygame.display.set_mode((500, 500))
        # Instantiate a clock object
        self.clock = pygame.time.Clock()
        # Load the image to be blitted later
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        # Set a starting position for the image
        self.img_pos = [160, 260]
        # Initiate movement in [x, y] format
        self.movement = [False, False]
        # Set specified RGB value to transparent
        self.img.set_colorkey((0, 0, 0))
        # Draw rectangle which acts as our collision box
        self.collision_area = pygame.Rect(50, 50, 300, 50)



    def run(self):
        while True:

            # Fill the screen with a light blue color
            self.screen.fill((14, 219, 248))

            # Create a rectangle that overlaps our object for collision purposes
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            # Check if the overlapped collision box is colliding with the predefined collision area, change color of collision area based on condition
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 255), self.collision_area)                


            # Check for user input
            for event in pygame.event.get():
                # Check if user wants to exit program
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Check if key is pressed down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                # Check if key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False


            # Update image position based on movement values
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5

            # Blit image onto the screen at the updated position
            self.screen.blit(self.img, self.img_pos)

            # Update the display
            pygame.display.update()
            # Set FPS
            self.clock.tick(60)

# Run the game
Game().run()

