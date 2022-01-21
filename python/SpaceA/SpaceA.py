# Космическая одиссея "SpaceA" автор З.П.А. гр.22928/1
import pygame
import random
from os import path
from actors import *
from setings import *


# Создание игры и окна
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" КОСМИЧЕСКАЯ ОДИССЕЯ")
clock = pygame.time.Clock()

#background = pygame.image.load(path.join(img_dir, "locationP.png")).convert()
#background_rect = background.get_rect()

player = Player()
all_sprites.add(player)
#список для создания астероидов
for i in range(12):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
#список для создания звёздочек
for i in range(23):
    s =Star()
    all_sprites.add(s)
    stars.add(s)

# Цикл игры
running = True
while running:
    # Цикл на скорости  FPS
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # стрельба
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Обновление
    all_sprites.update()
    # группа для взаимодействия с кораблем
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

