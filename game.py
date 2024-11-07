# Import and initialize pygame
import pygame
pygame.init()

# Configure the screen
# screen = pygame.display.set_mode([500, 500])

# Create the game loop
# running = True
# while running:
#     # Looks at events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running == False

#     # Clear the screen - expressed as a tuple
#     screen.fill((255, 255, 255))
#     # Draw a circle - assigned a tuple
#     color = (255, 0, 255)
#     # Assigned a tuple but with two vaules x and y
#     position = (250, 250)
#     pygame.draw.circle(screen, color, position, 75)
#     # Update the display
#     pygame.display.flip()

#     # Clear the screen - expressed as a tuple - color bright red
#     screen.fill((255, 255, 255))
#     # Draw a circle - assigned a tuple
#     color = (255, 0, 0)
#     # Assigned a tuple but with two vaules x and y
#     position = (100, 100)
#     pygame.draw.circle(screen, color, position, 75)
#     # Update the display
#     pygame.display.flip()

# # Draw a circle - assigned a tuple - color orange
#     color = (255, 145, 0)
#     # Assigned a tuple but with two vaules x and y
#     position = (400, 100)
#     pygame.draw.circle(screen, color, position, 75)
#     # Update the display
#     pygame.display.flip()

# # Draw a circle - assigned a tuple - color yellow
#     color = (250, 218, 7)
#     # Assigned a tuple but with two vaules x and y
#     position = (280, 300)
#     pygame.draw.circle(screen, color, position, 75)
#     # Update the display
#     pygame.display.flip()

# # Draw a circle - assigned a tuple - bright green
#     color = (0, 255, 0)
#     # Assigned a tuple but with two vaules x and y
#     position = (100, 400)
#     pygame.draw.circle(screen, color, position, 75)
#     # Update the display
#     pygame.display.flip()

# # Draw a circle - assigned a tuple - color navy blue
#     color = (0, 0, 255)
#     # Assigned a tuple but with two vaules x and y
#     position = (400, 400)
#     pygame.draw.circle(screen, color, position, 75)
#     # Update the display
#     pygame.display.flip()

screen = pygame.display.set_mode((500, 500))  # 500x500 window for a 3x3 grid
screen.fill((255, 255, 255))  # White background

# Circle settings
circle_radius = 45
circle_color = (105, 105, 105)  # Dark gray color
circle_spacing = 200  # Space between circles

# Single loop to place circles in a 3x3 grid
for i in range(9):  # 9 circles in total for a 3x3 grid - loops from 0 to 8(9 total iterations)
    row = i // 3  # Calculate row (0, 1, 2) 
    col = i % 3   # Calculate column (0, 1, 2) 
    x = col * circle_spacing + circle_radius  # Calculate x position - places circles at intervals of circle_spacing (100 pixels) horizontally adding circle_radius (30 pixels) to center 
    y = row * circle_spacing + circle_radius  # Calculate y position - " "
    pygame.draw.circle(screen, circle_color, (x, y), circle_radius)

pygame.display.flip()  # Update the display to show the circles

# Keep the window open until the user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()