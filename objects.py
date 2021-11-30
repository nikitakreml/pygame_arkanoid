import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, texture, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.is_scored = False
        self.speed = self.speedX, self.speedY = 3, 3
        self.width = 100
        self.height = 70
        self.x = x
        self.y = y
        self.is_alive = True
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.y = self.y
        self.rect.x = self.x

    def collision(self, collided_sprite):
        if pygame.sprite.collide_circle(self, collided_sprite):
            pygame.sprite.Sprite.kill(self)
            collided_sprite.speedY = -collided_sprite.speedY
            self.is_alive = False

    def update(self, collided_sprite):
        self.collision(collided_sprite)


class Ball(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y, width, height, screen_w, screen_h):
        pygame.sprite.Sprite.__init__(self)
        self.speed = self.speedX, self.speedY = 7, 7
        self.x = player_x
        self.y = player_y
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.image = pygame.image.load('Assets/purple_ball_texture.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.y = self.y
        self.rect.x = self.x

        self.is_alive = True
        self.lives = 3

    def collision(self, collided_sprite, screen_width, screen_height):
        if pygame.sprite.collide_mask(self, collided_sprite):
            self.speedY = -self.speedY
            self.rect.y = collided_sprite.rect.y
        if self.rect.x <= 0 or self.rect.x >= screen_width - self.rect.width:
            self.speedX = -self.speedX
        if self.rect.y <= 0:
            self.speedY = -self.speedY
        if self.rect.y >= screen_height - self.rect.height:
            self.lives -= 1
            self.rect.x = self.x
            self.rect.y = self.y

    def update(self, collided_sprite):
        self.collision(collided_sprite, self.screen_w, self.screen_h)
        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if self.lives == 0:
            self.is_alive = False


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, normal_speed):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.normal_speed = normal_speed
        self.move_speed = 0
        self.image = pygame.image.load("Assets/platform.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def controls(self, e):
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                self.move_speed = 0
            if e.key == pygame.K_d:
                self.move_speed = 0

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                self.move_speed = -self.normal_speed
            if e.key == pygame.K_d:
                self.move_speed = self.normal_speed

    def update(self):
        self.rect.x += self.move_speed