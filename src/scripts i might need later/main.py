# Import pygame
import pygame, sys

# Initialise pygame
pygame.init()

# Import level data
from data import data

# Game variables
screen_size = [800, 480]
clock = pygame.time.Clock()
fps = 60

# Set window caption and size
pygame.display.set_caption('Lord of the Frisbees')
display = pygame.display.set_mode(screen_size)

cameraOffset = 0
tileSize = 48

# Load character and npc sprites
sprites = {
    'left': {
        'idle': pygame.transform.scale(pygame.image.load('assets/sprites/rightIdle.png'), (36, 96)),
        'run': [
            pygame.transform.scale(pygame.image.load('assets/sprites/rightIdle.png'), (36, 96)),
            pygame.transform.scale(pygame.image.load('assets/sprites/rightIdle.png'), (36, 96))
        ]
    },
    'right': {
        'idle': pygame.transform.scale(pygame.image.load('assets/sprites/rightIdle.png'), (36, 96)),
        'run': [
            pygame.transform.scale(pygame.image.load('assets/sprites/rightIdle.png'), (36, 96)),
            pygame.transform.scale(pygame.image.load('assets/sprites/rightIdle.png'), (36, 96))
        ]
    }
}

nythanSprites = {}
philSprites = {}
erikSprites = {}
savasSprites = {}

dirtImg = pygame.transform.scale(pygame.image.load('assets/sprites/dirt.png'), (48, 48))
grassImg = pygame.transform.scale(pygame.image.load('assets/sprites/grass.png'), (48, 48))

class World:
    def __init__(self, data):
        self.tiles = []

        x = 1
        y = 1
        
        # Create world
        for row in data:
            x = 0
            
            for tile in row:
                if tile == 1:
                    img = dirtImg
                    img_rect = img.get_rect()

                    img_rect.x = x * tileSize
                    img_rect.y = y * tileSize

                    tile = [img, img_rect, 'dirt']

                    self.tiles.append(tile)

                if tile == 2:
                    img = grassImg
                    img_rect = img.get_rect()

                    img_rect.x = x * tileSize
                    img_rect.y = y * tileSize

                    tile = [img, img_rect, 'grass']

                    self.tiles.append(tile)
                
                x += 1
            y += 1

    def draw(self):
        for tile in self.tiles:
            display.blit(tile[0], (tile[1].x - cameraOffset, tile[1].y))

world = World(data)

class Player:
    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.grounded = False
        self.direction = 'right'
        self.img = sprites[self.direction]['idle']
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step = 0
        self.run = 0
        self.gravity = 0

    def draw(self):
        # This crap changes the run sprite between two images
        self.step += 1

        if (self.step > 10): self.run = 1
        else: self.run = 0

        if (self.step > 20): self.step = 1

        # Reset delta X and Y
        self.dx = 0
        self.dy = 0

        # Get all pressed keys
        key = pygame.key.get_pressed()

        # Input handler
        if key[pygame.K_a]:
            self.dx -= 5
            self.direction = 'left'
            #self.img = sprites[self.direction][run][self.step]

        if key[pygame.K_d]:
            self.dx += 5
            self.direction = 'right'
            #self.img = sprites[self.direction][run][self.step]

        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.img = sprites[self.direction]['idle']

        if key[pygame.K_SPACE]:
            if self.grounded:
                self.gravity = -12

        if (self.gravity < 15):
            self.gravity += 1

        self.dy += self.gravity

        self.grounded = False

        # Collision detection
        for tile in world.tiles:
            # Collision in X axis
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, 36, 92):
                self.dx = 0

            # Collision in Y axis
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, 36, 92):
                if self.gravity < 0:
                    self.gravity = 0
                    self.dy = tile[1].bottom - self.rect.top

                elif self.gravity >= 0:
                    self.grounded = True
                    self.gravity = 0
                    self.dy = tile[1].top - self.rect.bottom

        # Update coords
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Display player sprite
        display.blit(self.img, self.rect)

player = Player(150, 150)

# Game loop
Running = True
while Running:
    display.fill((69, 180, 250))

    player.draw()
    world.draw()

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    # Maintain fps
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
sys.exit()