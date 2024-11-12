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


class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.dx = 0
        self.dy = 0
        self.reset()

    def left(self):
        self.dx -= 100

    def right(self):
        self.dx += 100

    def up(self):
        self.dy -= 100

    def down(self):
        self.dy += 100

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32


#  Instance of GameObject
apple = GameObject(0, 250, 'apple.png')


# Instance of fruit
apple = Apple()

# Instance of player
player = Player()


    # Clear screen
screen.fill((255, 255, 255))

# Create the game loop
running = True
while running:
  # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running == False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # Draw apple
    apple.move()
    apple.render(screen)

    # Draw player
    player.move()
    player.render(screen)

    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)

