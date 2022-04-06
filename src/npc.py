class NPC:
    def __init__(self, x, y, sprites, name, _def, atk, speed, jump_power):
        self.sprites = sprites
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self._def = _def
        self.atk = atk
        self.direction = 'left'
        self.img = sprites[self.direction]['idle']
        self.attacked = False
        self.dx = 0
        self.dy = 0
        self.gravity = 0
        self.speed = speed
        self.jump_power = jump_power
        self.alive = True

    def kill(self):
        self.alive = False

    def respawn(self):
        self.alive = True

    def update(self, world, player):
        if not self.alive: return

        self.dx = 0
        self.dy = 0

        if (self.gravity < 15):
            self.gravity += 1

        self.dy += self.gravity

        self.grounded = False

        # If the player has attacked the NPC
        if (self.attacked):
            '''
            Calculate if the player is to the right or left

            Go towards player

            If there is a block, jump over it

            If there is void, don't follow the player into the void

            If player is less than 0.5 tiles away, punch

            If more than 0.5 tiles away, use a ranged attack
            '''
            pass

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

    def draw(self, display, world):
        display.blit(self.img, (self.rect.x - world.camera_offset[0], self.rect.y - self.camera_offset[1]))