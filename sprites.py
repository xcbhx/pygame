from random import randint
import pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Get the clock
clock = pygame.time.Clock()


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        # self.surf = pygame.Surface((width, height))
        # self.surf.fill((255, 0, 255))
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the apple
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = randint(50, 400)
        self.y = -64



#  Instance of GameObject
# box = GameObject(120, 300, 50, 50)
apple = GameObject(0, 250, 'apple.png')
apple1 = GameObject(0, 100, 'apple.png')
strawberry = GameObject(200, 100, 'strawberry.png')
apple1 = GameObject(400, 100, 'apple.png')
strawberry1 = GameObject(0, 250, 'strawberry.png')
apple2 = GameObject(200, 240, 'apple.png')
strawberry2 = GameObject(400, 240, 'strawberry.png')
apple3 = GameObject(0, 400, 'apple.png')
strawberry3 = GameObject(210, 400, 'strawberry.png')
apple4 = GameObject(400, 400, 'apple.png')

# Instance of Fruit instances
apple = Apple()

    # Clear screen
screen.fill((255, 255, 255))

# Create the game loop
running = True
while running:
  # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    apple1.render(screen)
    strawberry.render(screen)
    apple1.render(screen)
    strawberry1.render(screen)
    apple2.render(screen)
    strawberry2.render(screen)
    apple3.render(screen)
    strawberry3.render(screen)
    apple4.render(screen)


    apple.x += 1.8
    apple.render(screen)


    # Draw apple
    apple.move()
    apple.render(screen)

    # Draw box
    # box.render(screen)

    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)

