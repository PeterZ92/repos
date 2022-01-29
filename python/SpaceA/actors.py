#actors.py файл с классами игровых объектов
import pygame
import random
from os import path
from setings import*


# класс игорок
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius=25#AABB радиус для корабля
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)# визуализация ААВВ игрока(граница взаимодействия)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 60
        self.speedx = 0

# функция обновления и перемещения по оси Х
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
# функция стрельбы
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullet_2 = Bullet_rocet(self.rect.right, self.rect.top)
        bullet_3 = Bullet_rocet(self.rect.left, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        all_sprites.add(bullet_2)
        bullets.add(bullet_2)
        all_sprites.add(bullet_3)
        bullets.add(bullet_3)

# класс астероид
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = meteor_img
        self.image_orig.set_colorkey(WHITE)
        self.image= self.image_orig.copy()
        
        self.rect = self.image.get_rect()
        self.radius = int (self.rect.width* .9/2)#AABB радиус для астероида
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)# визуализация ААВВ астероида
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 7)
        self.speedx = random.randrange(-3, 3)
        #анимация вращения параметры
        self.rotation = 0
        self.rotation_speed= random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()
#функция отвечающая за вращение астероида
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update>50:
            self.last_update = now
            self.rotation=(self.rotation+self.rotation_speed)%360
            new_image=pygame.transform.rotate(self.image_orig,self.rotation)
            #self.image = pygame.transform.rotate(self.image_origin,self.rotation)
            old_center=self.rect.center
            self.image=new_image
            self.rect= self.image.get_rect()
            self.rect.center=old_center

# функция обновления
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 7)

# класс снаряды (пули)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = rocket_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

# функция обновления
    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

# класс снаряды (ракеты)
class Bullet_rocet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(bullet_images)
        self.image_orig.set_colorkey(WHITE)
        self.image= self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -17

# функция обновления
    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

# класс звездочки (для фона)
class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = stars_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, 695)
        self.speedy = 1
       
        # функция обновления
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-30, 0)
            self.speedy = 1
# группировка спрайтов
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
stars = pygame.sprite.Group()


