import pygame

playerSprites = {
    'left': {
        'idle': pygame.transform.scale(pygame.image.load('../assets/sprites/leftIdle.png'), (36, 96)),
        'run': [
            pygame.transform.scale(pygame.image.load('../assets/sprites/leftRun0.png'), (36, 96)),
            pygame.transform.scale(pygame.image.load('../assets/sprites/rightRun0.png'), (36, 96))
        ]
    },
    'right': {
        'idle': pygame.transform.scale(pygame.image.load('../assets/sprites/rightIdle.png'), (36, 96)),
        'run': [
            pygame.transform.scale(pygame.image.load('../assets/sprites/rightRun0.png'), (36, 96)),
            pygame.transform.scale(pygame.image.load('../assets/sprites/rightRun1.png'), (36, 96))
        ]
    }
}

nythanSprites = {}

philSprites = {}

erikSprites = {}

savasSprites = {}