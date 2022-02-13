import pygame, math, sys, os

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
bg = (69, 180, 250)
_world = world.World(data)
_player = player.Player(screen_size[0] / 2 - playerSprites['left']['idle'].get_width() / 2, screen_size[1] / 2 - playerSprites['left']['idle'].get_height() / 3, playerSprites, 100, 10, 5, 12)

# Import mods
mods_folder = os.listdir('mods/')

for file in mods_folder:
    if file.endswith('.py'):
        file = 'mods.' + file

        __import__(file[:-3])

# Set window caption and size
pygame.display.set_caption('Lord of the Frisbees')
display = pygame.display.set_mode(screen_size)

# Game loop
Running = True
while Running:
    # Draw the background
    display.fill(bg)

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