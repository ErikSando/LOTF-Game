import pygame, sys

# Initialise pygame
pygame.init()

# Import game files
import world, player, npc

# Import world data
from data import data
from sprites import playerSprites, philSprites, nythanSprites, erikSprites, savasSprites

# Game variables
screen_size = [800, 480]
clock = pygame.time.Clock()
fps = 60

# Set window caption and size
pygame.display.set_caption('Lord of the Frisbees')
display = pygame.display.set_mode(screen_size)

_world = world.World(data)
_player = player.Player(50, 50, playerSprites)

# Game loop
Running = True
while Running:
    # Draw the background
    display.fill((69, 180, 250))

    # Render player and world
    _player.draw(display, _world)
    _world.draw(display)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    # Maintain fps
    clock.tick(fps)

    # Update display
    pygame.display.update()
pygame.quit()
sys.exit()