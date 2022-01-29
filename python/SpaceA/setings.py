# setings.py (файл с настройками)
import pygame
import random
from os import path

#директория для поиска файлов
img_dir = path.join(path.dirname(__file__), 'bmpN')

# параметры окна и скорости кадров
WIDTH = 500
HEIGHT = 700
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (5, 5, 80) #(0,0,255)
YELLOW = (240, 240, 30) #(255,255,0)

# функция посчета очков
font_name=pygame.font.match_font('arial')
def show_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,BLUE)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)


# Загрузка изображений
background = pygame.image.load(path.join(img_dir, "locationP.png"))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "sship2.png"))
meteor_img = pygame.image.load(path.join(img_dir, "asteroid.bmp"))#при png не правильная работа анимации
#bullet_img = pygame.image.load(path.join(img_dir, "bullet.png"))#обычные патроны
rocket_img = pygame.image.load(path.join(img_dir, "rokcets.png"))
stars_img = pygame.image.load(path.join(img_dir, "stars_e.png"))

#цветные патроны
bullet_images = []
bullet_list=['b_gr.bmp','b_or.bmp','b_red.bmp','b_vio.bmp','bullet.bmp']
for  img in bullet_list:
    bullet_images.append(pygame.image.load(path.join(img_dir, img)))

