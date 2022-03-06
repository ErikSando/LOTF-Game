import game, player, sprites

defence = 100 # Edit this to change player health

x = game._player.rect.x
y = game._player.rect.y
sprites = game._player.sprites
_def = defence
atk = game._player.atk
speed = game._player.speed
jump_power = game._player.jump_power

game._player = player.Player(x, y, sprites, _def, atk, speed, jump_power)