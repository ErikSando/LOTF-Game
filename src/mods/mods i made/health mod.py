import game, player, sprites

defence = 100000000000000 # Edit this to change player health

x = game._player.rect.x
y = game._player.rect.y
sprites = game._player.sprites
_def = game._player._def
atk = game._player.atk
speed = game._player.speed
jump_power = game._player.jump_power

game._player = player.Player(x, y, sprites, _def, atk, speed, jump_power)