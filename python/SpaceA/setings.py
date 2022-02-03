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

# таймер для бонуса стрельбы
UP_GUN = 5000

# функция посчета очков
font_name=pygame.font.match_font('arial')
def show_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,BLUE)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)
#индикатор брони
def show_shell(surf,x,y,pct):
    if pct<0:
        pct=0
    BAR_LENGHT=100
    BAR_HEIGHT=25
    fill=(pct/100)*BAR_LENGHT
    outline_rect= pygame.Rect(x,y,fill,BAR_HEIGHT)
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,BLUE,fill_rect)
    pygame.draw.rect(surf,BLUE,outline_rect,2)

#индикатор здоровья
def show_hp(surf,x,y,pct):
    if pct<0:
        pct=0
    BAR_LENGHT=100
    BAR_HEIGHT=25
    fill=(pct/100)*BAR_LENGHT
    outline_rect= pygame.Rect(x,y,fill,BAR_HEIGHT)
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,RED,fill_rect)
    pygame.draw.rect(surf,RED,outline_rect,2)


# Загрузка изображений
background = pygame.image.load(path.join(img_dir, "locationP.png"))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "sship2.png"))
meteor_img = pygame.image.load(path.join(img_dir, "asteroid.bmp"))#при png не правильная работа анимации
#bullet_img = pygame.image.load(path.join(img_dir, "bullet.png"))#обычные патроны
rocket_img = pygame.image.load(path.join(img_dir, "rokcets.png"))
stars_img = pygame.image.load(path.join(img_dir, "stars_e.png"))
shell_img = pygame.image.load(path.join(img_dir, "enrj_vio.png"))
hp_img = pygame.image.load(path.join(img_dir, "hp_red.png"))

#цветные патроны
bullet_images = []
bullet_list=['b_gr.bmp','b_or.bmp','b_red.bmp','b_vio.bmp','bullet.bmp']
for  img in bullet_list:
    bullet_images.append(pygame.image.load(path.join(img_dir, img)))

# анимация взрыва
exp_ani={}
exp_ani['big']=[]
exp_ani['small']=[]
for i in range(6):
    filename= 'exp{}.bmp'.format(i)
    img=pygame.image.load(path.join(img_dir,filename))
    img.set_colorkey(WHITE)
    img_big=pygame.transform.scale(img,(80,80))
    exp_ani['big'].append(img_big)
    img_small=pygame.transform.scale(img,(50,50))
    exp_ani['small'].append(img_small)

# словарь с изображениями для бонусов
bonus_immages={}
bonus_immages['shell']=pygame.image.load(path.join(img_dir,'enrg.bmp'))
bonus_immages['hp']=pygame.image.load(path.join(img_dir,'hp.bmp'))
bonus_immages['gun']=pygame.image.load(path.join(img_dir,'gun.bmp'))#####




