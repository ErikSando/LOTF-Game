# Import pygame
import pygame

# Initialise pygame
pygame.init()

cameraOffset = 0
tileSize = 48

# Load sprites
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

    def draw(self, display):
        for tile in self.tiles:
            display.blit(tile[0], (tile[1].x - cameraOffset, tile[1].y))