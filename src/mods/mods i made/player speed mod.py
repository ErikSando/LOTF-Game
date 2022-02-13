import game, player

print('hi')

speed = 10          # Default = 5
jump_power = 24     # Default = 12

# Get the current player values
x = game._player.rect.x
y = game._player.rect.y
sprites = game._player.sprites
_def = game._player._def
atk = game._player.atk

game._player = player.Player(x, y, sprites, _def, atk, speed, jump_power)