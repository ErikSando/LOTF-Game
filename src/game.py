import pygame, math, sys, os

# Initialise pygame
pygame.init()

# Import game files
import world_generator, world, player, npc, data
# Uncomment this to make the game work
# data = data.data
data = world_generator.generate_world()

# Import world data
from sprites import playerSprites, philSprites, nythanSprites, erikSprites, savaSprites

# Game variables
screen_size = [800, 480]
clock = pygame.time.Clock()
fps = 60
bg = (69, 180, 250)
_world = world.World(data)
_player = player.Player(screen_size[0] / 2 - playerSprites['left']['idle'].get_width() / 2, screen_size[1] / 2 - playerSprites['left']['idle'].get_height() / 3, playerSprites, 100, 10, 5, 12)
npcs = []

# Import mods
mods_folder = os.listdir('mods/')

for file in mods_folder:
    if file.endswith('.py'):
        file = 'mods.' + file

        __import__(file[:-3])

# Set window caption and size
pygame.display.set_caption('Lord of the Frisbees')
display = pygame.display.set_mode(screen_size)

# def rect_intersection(r1, r2):
#     if (r1.x + r1.w < r2.x or
#         r1.x > r2.x + r2.w or
#         r1.y + r1.h < r2.y or
#         r1.y > r2.y + r2.h): return False

#     return True

# Game loop
Running = True
while Running:
    # Draw the background
    display.fill(bg)

    # Render player and world
    _player.update(_world)
    
    _world.draw(display)
    _player.draw(display)

    for _npc in npcs:
        _npc.update(_world)
        _npc.draw(display)

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