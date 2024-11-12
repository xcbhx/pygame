from random import randint, choice
import pygame
pygame.init()

lanes = [93, 218, 343]


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
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y 
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
        self.x = choice(lanes)
        self.y = -64


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the strawberry
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = -64

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.gif')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the strawberry
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = -64


class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.dx = 0
        self.dy = 0
        self.pos_x = 1 
        self.pos_y = 1
        self.reset()

    def left(self):
        if self.pos_x > 0:
                self.pos_x -= 1
                self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
                self.pos_x += 1
                self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
                self.pos_y -= 1
                self.update_dx_dy()

    def down(self):
	    if self.pos_y < len(lanes) - 1:
                self.pos_y += 1
                self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]



#  Instance of GameObject
apple = Apple()
strawberry = Strawberry()
bomb = Bomb()
player = Player()

# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

# make a fruits Group
fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)



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

    # Clear screen
    screen.fill((255, 255, 255))
    # Move and render Sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Check Colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()
    
    # Check collision player and bomb
    if pygame.sprite.collide_rect(player, bomb):
        running = False

    # Update the window
    pygame.display.flip()

    # tick the clock!
    clock.tick(60)

