# Import pygame
import pygame

# Initialise pygame
pygame.init()

# Load character sprites
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

run = 0

class Player:
    def __init__(self, x, y, sprites, _def, atk, speed, jump_power):
        self.dx = 0
        self.dy = 0
        self.grounded = False
        self.sprites = sprites
        self.direction = 'right'
        self.img = self.sprites[self.direction]['idle']
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.step = 0
        self.run = 0
        self.gravity = 0
        self._def = _def
        self.atk = atk
        self.speed = speed
        self.jump_power = jump_power

    def draw(self, display, world):
        # This crap changes the run sprite between two images
        self.step += 1

        if (self.step > 10): self.run = 1
        else: self.run = 0

        if (self.step > 20): self.step = 1

        # Reset delta X and Y
        self.dx = 0
        self.dy = 0

        # Increase force of gravity
        if (self.gravity < 15):
            self.gravity += 1

        # Get all pressed keys
        key = pygame.key.get_pressed()

        # Input handler
        if key[pygame.K_a]:
            self.dx -= self.speed
            self.direction = 'left'
            #self.img = sprites[self.direction][run][self.step]

        if key[pygame.K_d]:
            self.dx += self.speed
            self.direction = 'right'
            #self.img = sprites[self.direction][run][self.step]

        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.img = self.sprites[self.direction]['idle']

        if key[pygame.K_SPACE]:
            if self.grounded:
                self.gravity = -self.jump_power

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