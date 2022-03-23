# Космическая одиссея "SpaceA" автор З.П.А. гр.22928/1
# файл SpaceA.py основной файл
import pygame
import random
from os import path
from actors import*
from setings import *

# Создание игры и окна
pygame.init()
pygame.mixer.init()
pygame.display.set_caption(" КОСМИЧЕСКАЯ ОДИССЕЯ")

#background = pygame.image.load(path.join(img_dir, "locationP.png")).convert()
#background_rect = background.get_rect()
def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

player = Player()
all_sprites.add(player)

s= Shell_icon()
all_sprites.add(s)

h= Hp_icon()
all_sprites.add(h)

#список для создания астероидов
for i in range(difficults):
    newmob()
#список для создания звёздочек
for i in range(23):
    s =Star()
    all_sprites.add(s)
    stars.add(s)
# score  переменная для посчета очков
score = 0 
# Цикл игры
pause= False
game_over = True
running = True

while running:
   
   
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites.add(player)
        player.hp=100
        player.shell=100
        
        #Запись очков в файл конец
        score = 0
    if pause:
        pause= False
        pause_screen(str(score))
        
 # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        #button_update()
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #Запись очков в файл
                if score>100:
                   s_rec= open('records.txt','a')
                   s_rec.write(str(score) + '\n')
                   s_rec.close()
                game_over=True
                show_go_screen()
            if event.key == pygame.K_p:
                pause= True
                pause_screen(str(score))
                

    # Обновление
    all_sprites.update()
    # группа для взаимодействия с кораблем
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 10 # + 10 очков за каждый астероид
        ex=Exp(hit.rect.center,'big')
        all_sprites.add(ex)
        # условие случайности появление бонуса 10%
        if random.random()>0.9:
            bon= Bonus(hit.rect.center)
            all_sprites.add(bon)
            bonus.add(bon)
        # newmob() чтобы астероиды не исчезали после уничтожения
        newmob()

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, True ,pygame.sprite.collide_circle)
    for hit in hits:
        if hits:
            player.shell-=20#///////////////////////////
            expl=Exp(hit.rect.center,'small')
            all_sprites.add(expl)
            newmob()
            if player.shell<0:
                if hits:
                    player.hp-=50
                    newmob()
                    if player.hp<=0:                       
                       player_exp=Exp(player.rect.center,'big')
                       all_sprites.add(player_exp)
                       #Запись очков в файл
                       if score>100:
                           s_rec= open('records.txt','a')
                           s_rec.write(str(score) + '\n')
                           s_rec.close()
                   
                      #завершение игрового цикла
                       game_over = True
        

    # проверка столкновения с бонусом
    hits = pygame.sprite.spritecollide(player,bonus , True)
    for hit in hits:
        if hit.type =='shell':
            player.shell=100
        if hit.type =='hp':
            player.hp=100
        if hit.type == 'gun':
            player.powerup()

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    show_text(screen,str(score),25,WIDTH/2,670)
    show_shell(screen,40,670,player.shell)
    show_hp(screen,360,670,player.hp)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

