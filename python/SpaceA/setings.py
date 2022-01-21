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
BLUE = (0, 120, 255) #(0,0,255)
YELLOW = (255, 255, 70) #(255,255,0)

# Загрузка изображений
background = pygame.image.load(path.join(img_dir, "locationP.png"))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "sship2.png"))
meteor_img = pygame.image.load(path.join(img_dir, "asteroid.png"))
bullet_img = pygame.image.load(path.join(img_dir, "bullet.png"))
rocket_img = pygame.image.load(path.join(img_dir, "rokcets.png"))
stars_img = pygame.image.load(path.join(img_dir, "stars_e.png"))
