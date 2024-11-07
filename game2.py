# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Create the game loop
running = True
while running:
  # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw a circle
    screen.fill((255, 255, 255))

    # Update the window
    pygame.display.flip()

    # Create a new instance of Surface
    surf = pygame.Surface((50, 50))
    surf.fill((255, 111, 33))

    # Clear screen
    screen.fill((255, 255, 255))
    # Draw the surface
    screen.blit(surf, (100, 120))

    # Update the window
    pygame.display.flip()