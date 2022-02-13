import pygame

playerSprites = {
    'left': {
        'idle': pygame.transform.scale(pygame.image.load('../assets/sprites/rightIdle.png'), (36, 96)),
        'run': [
            pygame.transform.scale(pygame.image.load('../assets/sprites/rightIdle.png'), (36, 96)),
            pygame.transform.scale(pygame.image.load('../assets/sprites/rightIdle.png'), (36, 96))
        ]
    },
    'right': {
        'idle': pygame.transform.scale(pygame.image.load('../assets/sprites/rightIdle.png'), (36, 96)),
        'run': [
            pygame.transform.scale(pygame.image.load('../assets/sprites/rightIdle.png'), (36, 96)),
            pygame.transform.scale(pygame.image.load('../assets/sprites/rightIdle.png'), (36, 96))
        ]
    }
}

nythanSprites = {}

philSprites = {}

erikSprites = {}

savasSprites = {}