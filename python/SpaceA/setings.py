# setings.py (файл с настройками)
import pygame
import random
from button_class import*
from os import path

#директория для поиска файлов
img_dir = path.join(path.dirname(__file__), 'bmpN')

# параметры окна и скорости кадров
WIDTH = 500
HEIGHT = 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (5, 5, 80) #(0,0,255)
YELLOW = (127, 255, 210) #светло голубой
MIXCOLOR =(150,90,180)# оттенок фиолетового
OLIVE =(85,110,50)# оливковый

# таймер для бонуса стрельбы
UP_GUN = 5000

# переменые для уровня сложности
difficults = 12


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

       
# кнопички
St=Button(RED,2,0,120,50,'НАСТРОЙКИ')
Rec_s=Button(RED,127,0,120,50,'РЕКОРДЫ')
About=Button(RED,252,0,120,50,'СПРАВКА')
Quit=Button(RED,377,0,120,50,'ВЫХОД')
Back=Button(RED,377,0,120,50,'НАЗАД')
Dif_colour=Button(RED, 190,170,120,50,'КР/ЗЕЛ')
Dif_colour_2=Button(RED, 190,265,120,50,'НЕБ/ФИО')
update_record= Button(RED, 150,500,200,50,'СБРОСИТЬ РЕКОРДЫ')



# экран основного меню
def show_go_screen():
    screen.blit(background, background_rect)
    show_text(screen, "КОСМИЧЕСКАЯ ОДИССЕЯ", 40, WIDTH / 2, HEIGHT / 4)
    show_text(screen, "курсовой проект:)", 22,
              WIDTH / 2, HEIGHT / 2)
    show_text(screen, "любая клавиша для старта", 18, WIDTH / 2, HEIGHT * 3 / 4)
    # ОТОБРАЖЕНИЕ КНОПОК НА ГЛАВНОМ ЭКРАНЕ
    St.draw(screen,)
    Rec_s.draw(screen)
    About.draw(screen)
    Quit.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
    waiting = True
   # clock.tick(FPS)
    while waiting:
        # зоны для обновления экрана
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
            if event.type== pygame.MOUSEMOTION:
                
                if Quit.klik(pos):
                    Quit.color=(GREEN)
                    Quit.draw(screen)
                    print('Q')
                   
                else:
                    Quit.color=(RED)
                    Quit.draw(screen)

                if St.klik(pos):
                    St.color=(GREEN)
                    St.draw(screen)
                    print('S')
                   
                else:
                    St.color=(RED)
                    St.draw(screen)

                if Rec_s.klik(pos):
                    Rec_s.color=(GREEN)
                    Rec_s.draw(screen)
                    print('R')
                   
                else:
                    Rec_s.color=(RED)
                    Rec_s.draw(screen)

                if About.klik(pos):
                    About.color=(GREEN)
                    About.draw(screen)
                    print('A')
                   
                else:
                    About.color=(RED)
                    About.draw(screen)

            if event.type==pygame.MOUSEBUTTONDOWN:
               
                if Quit.klik(pos):
                    waiting=False
                    pygame.quit()

                if St.klik(pos):
                    waiting=False
                    seting_screen()

                if About.klik(pos):
                    waiting=False
                    about_screen()

                if Rec_s.klik(pos):
                    waiting=False
                    recs_screen()

# экран паузы
def pause_screen(s):

    screen.blit(background, background_rect)
    show_text(screen,"ОЧКИ: "+ s, 40, WIDTH/2 , 40)
    show_text(screen, "КОСМИЧЕСКАЯ ОДИССЕЯ", 40, WIDTH / 2, HEIGHT / 5)
    show_text(screen, "ПАУЗА!", 22,
              WIDTH / 2, HEIGHT / 2)
    show_text(screen, "любая клавиша для старта", 18, WIDTH / 2, HEIGHT * 3 / 4)
   # St.draw(screen)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# экран настроек
def seting_screen():
    screen.blit(background, background_rect)
    show_text(screen, "НАСТРОЙКИ ТЕМЫ", 40, WIDTH / 2, 100)
    show_text(screen, "СБРОС РЕКОРДОВ", 40, WIDTH / 2, 430)
    show_text(screen, "красно-зеленый: тема 1 (по умолчанию)", 22,
              WIDTH / 2, 340)
    show_text(screen, "небесно-фиолетовый: тема 2", 22,
              WIDTH / 2, 375)
    show_text(screen, "ВНИМАНИЕ! при нажатии сбросятся рекорды", 22,
              WIDTH / 2, 570)
    show_text(screen, "ESCAPE для возврата в меню", 18, WIDTH / 2, 650)
    Back.draw(screen)
    Dif_colour.draw(screen)
    Dif_colour_2.draw(screen)
    update_record.draw(screen)
  
    pygame.display.flip()
    clock.tick(FPS)
    waiting = True
    while waiting:
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                waiting=False#////////////
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    show_go_screen()

            elif event.type== pygame.MOUSEBUTTONDOWN:
                global RED
                global GREEN
                global BLUE
                if Back.klik(pos):
                    waiting = False
                    show_go_screen()
                   
                if Dif_colour.klik(pos):
                    RED = (255, 0, 0)
                    GREEN = (0, 255, 0)
                    BLUE=(5, 5, 80)
                    Dif_colour.color=(GREEN)
                    Dif_colour_2.color=(RED)
                    Dif_colour.draw(screen)
                    Dif_colour_2.draw(screen)
                    pygame.display.update()

                    
                if Dif_colour_2.klik(pos):
                    RED=MIXCOLOR
                    GREEN = YELLOW
                    BLUE= OLIVE
                    Dif_colour.color=(RED)
                    Dif_colour_2.color=(GREEN)
                    Dif_colour.draw(screen)
                    Dif_colour_2.draw(screen)
                    pygame.display.update()

                if update_record.klik(pos):
                    del_rec= open('records.txt','w')
                    del_rec.write('0'+'\n'+'0'+'\n'+'0'+'\n'+'0'+'\n'+'0'+'\n'+'0'+'\n')
                    del_rec.close()
                    print('records clear!!!!')

            elif event.type== pygame.MOUSEMOTION:
                
                if Back.klik(pos):
                    Back.color=(GREEN)
                    Back.draw(screen)
                    print('B')
                   
                else:
                    Back.color=(RED)
                    Back.draw(screen)

                if update_record.klik(pos):
                    update_record.color=(GREEN)
                    update_record.draw(screen)
                    print('rec')
                   
                else:
                    update_record.color=(RED)
                    update_record.draw(screen)

# экран об игре
def about_screen():
    screen.blit(background, background_rect)
    show_text(screen, "СПРАВКА И УПРАВЛЕНИЕ ", 40, WIDTH / 2, HEIGHT / 4)
    show_text(screen, "Как играть: сбивайте астероиды, собрайте бонусы, набирайте очки. ", 18, WIDTH / 2, 395)
    show_text(screen, "Следите за уровнем здоровья, столкновения губительны! ", 18, WIDTH / 2, 427)
    show_text(screen, "больше сбитых астероидов, больше очков! ", 18, WIDTH / 2, 460)
    show_text(screen, "При ошибке страницы рекордов:(НАСТРОЙКИ/СБРОСИТЬ РЕКОРДЫ!) ", 18, WIDTH / 2, 490)
    show_text(screen, "Движение корабля: стрелки (лево, право)", 18, WIDTH / 2, 235)
    show_text(screen, "Стрельба: пробел ", 18, WIDTH / 2, 265)
    show_text(screen, "Пауза: p ", 18, WIDTH / 2, 295)
    show_text(screen, "Меню: escape ", 18, WIDTH / 2, 328)
    show_text(screen, "ESCAPE для возврата в меню", 18, WIDTH / 2, 550)
    Back.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    waiting = True
    while waiting:
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    show_go_screen()
            elif event.type== pygame.MOUSEBUTTONDOWN:
                if Back.klik(pos):
                    waiting = False
                    show_go_screen()

            elif event.type== pygame.MOUSEMOTION:
                
                if Back.klik(pos):
                    Back.color=(GREEN)
                    Back.draw(screen)
                    print('B')
                   
                else:
                    Back.color=(RED)
                    Back.draw(screen)


#экран рекордов
def recs_screen():
    screen.blit(background, background_rect)
    rec_file_line=[]
    # октрытие файла с автоматическим закрытием
    with open("records.txt") as file_in:
        for re in file_in:
             rec_file_line.append(re)
    #перевод строк в число
    rec_in_int=[]
    for elements in rec_file_line:
        rec_in_int.append(int(elements))
    #сортировка
    rec_in_int.sort(reverse=True)
    print(rec_in_int)

   
    show_text(screen,str(rec_in_int[0]) , 22, WIDTH / 2, 270)
    show_text(screen,str(rec_in_int[1]) , 22, WIDTH / 2, 300)
    show_text(screen,str(rec_in_int[2]) , 22, WIDTH / 2, 330)
    show_text(screen,str(rec_in_int[3]) , 22, WIDTH / 2, 360)
    show_text(screen,str(rec_in_int[4]) , 22, WIDTH / 2, 390)
    show_text(screen, "РЕКОРДЫ", 40, WIDTH / 2, HEIGHT / 4)
    show_text(screen, "ESCAPE для возврата в меню", 18, WIDTH / 2, HEIGHT * 3 / 4)
    Back.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)
    waiting = True
    while waiting:
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    show_go_screen()
            elif event.type== pygame.MOUSEBUTTONDOWN:
                if Back.klik(pos):
                    waiting = False
                    show_go_screen()
               
                     

            elif event.type== pygame.MOUSEMOTION:
                
                if Back.klik(pos):
                    Back.color=(GREEN)
                    Back.draw(screen)
                    print('B')
                   
                else:
                    Back.color=(RED)
                    Back.draw(screen)

               




