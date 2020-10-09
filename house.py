import pygame 
from pygame.draw import *
import numpy as np

WHITE = (255, 255, 255)

pygame.init()  
FPS = 30
screen = pygame.display.set_mode((1500, 800))
screen.fill([135, 206, 250])
rect(screen, (66, 189, 84), (0, 400, 1500, 400))
i = 0

#house

def house(x, y, k):
    """
    Функция house рисует дом.
    х,у - координаты самой левой точки крыши
    k - масштаб домика
    """
    rect(screen, (150, 113, 23), (x, y, int(400*k), int(300*k)))
    rect(screen, (0, 0, 0), (x, y, int(400*k), int(300*k)), int(5*k))
    rect(screen, (95, 158, 169), (x+int(133*k), y+int(100*k), int(133*k), 
                                  int(100*k)))
    rect(screen, (181, 106, 53), (x+int(133*k), y+int(100*k), int(133*k), 
                                  int(100*k)), int(8*k))
    polygon(screen, (246, 74, 70), ((x, y), (x+int(400*k), y), 
                                    (x+int(200*k), y-int(200*k)), (x, y)))
    polygon(screen, (0, 0, 0), ((x, y), (x+int(400*k), y), 
                                (x+int(200*k), y-int(200*k)), (x, y)), 
            int(5*k))


#tree

def tree(x, y, k):
    """
    Функция tree рисует дерево.
    х,у - координаты верхнего левого угла ствола
    k - масштаб дерева
    """
    rect(screen, (0, 0, 0), (x, y, int(50*k), int(250*k)))
    circle(screen, (40, 114, 51), (x+int(20*k), y-int(200*k)), int(80*k))
    circle(screen, (0, 0, 0), (x+int(20*k), y-int(200*k)), int(80*k), int(3*k))
    circle(screen, (40, 114, 51), (x+int(100*k),y-int(140*k)), int(80*k))
    circle(screen, (0, 0, 0), (x+int(100*k),y-int(140*k)), int(80*k), int(3*k))
    circle(screen, (40, 114, 51), (x-int(65*k), y-int(140*k)), int(80*k))
    circle(screen, (0, 0, 0), (x-int(65*k), y-int(140*k)), int(80*k), int(3*k))
    circle(screen, (40, 114, 51), (x+int(20*k), y-int(110*k)), int(80*k))
    circle(screen, (0, 0, 0), (x+int(20*k), y-int(110*k)), int(80*k), int(3*k))
    circle(screen, (40, 114, 51), (x-int(40*k), y-int(50*k)), int(80*k))
    circle(screen, (0, 0 ,0), (x-int(40*k), y-int(50*k)), int(80*k), int(3*k))
    circle(screen, (40, 114, 51), (x+int(80*k), y-int(50*k)), int(80*k))
    circle(screen, (0, 0, 0), (x+int(80*k), y-int(50*k)), int(80*k), int(3*k))
    
    
#cloud
def cloud(x, y, k):
    """
    Функция cloud рисует облако.
    x,y - координаты центра первой окружности нарисованного облачка
    k - масштаб
    """
    circle(screen, (255, 255, 255), (x, y), int(80*k))
    circle(screen, (0, 0, 0), (x, y), int(80*k), int(3*k))
    circle(screen, (255, 255, 255), (x+int(90*k), y), int(80*k))
    circle(screen, (0, 0, 0), (x+int(90*k), y), int(80*k), int(3*k))
    circle(screen, (255, 255, 255), (x+int(180*k), y), int(80*k))
    circle(screen, (0, 0, 0), (x+int(180*k), y), int(80*k), int(3*k))
    circle(screen, (255, 255, 255), (x+int(270*k), y), int(80*k))
    circle(screen, (0, 0, 0), (x+int(270*k), y), int(80*k), int(3*k))
    circle(screen, (255, 255, 255), (x+int(190*k), y-int(70*k)), int(80*k))
    circle(screen, (0, 0, 0), (x+int(190*k), y-int(70*k)), int(80*k), int(3*k))
    circle(screen, (255, 255, 255), (x+int(85*k), y-int(70*k)), int(80*k))
    circle(screen, (0, 0, 0), (x+int(85*k), y-int(70*k)), int(80*k), int(3*k))
    
    
#sun

def sun(x, y, k):
    """
    Фунция sun рисует солнце.
    x,y - координаты центра солнца
    k - масштаб солнца
    """
    circle(screen, (255, 255, 0), (x, y), int(50*k))
    n = 20
    for i in range(0, n, 1):
        alpha = 2*np.pi/n
        x1 = x + 50*k*np.cos(i*alpha)
        y1 = y + 50*k*np.sin(i*alpha)
        x2 = x + 50*k*np.cos((i+0.6)*alpha)
        y2 = y + 50*k*np.sin((i+0.6)*alpha)
        x3 = x + 60*k*np.cos((i+0.3)*alpha)
        y3 = y + 60*k*np.sin((i+0.3)*alpha)
        polygon(screen, (255, 255, 0), ((x1,y1), (x2, y2), (x3, y3)))

#sky color

def sky_color(cloud_x):
    if cloud_x < 100:
        screen.fill([135 - int(7*cloud_x/100),
                     206 - int(33*cloud_x/100),
                     250 - int(15*cloud_x/100)])

    else:
        screen.fill([128 + int(7*(cloud_x-100)/100),
                     173 + int(33*(cloud_x-100)/100),
                     235 + int(15*(cloud_x-100)/100)])

#field color

def field_color(cloud_x):
    if cloud_x<100:
        rect(screen, (66 - int(13*cloud_x/100), 
                      189 - int(37*cloud_x/100), 
                      84 - int(16*cloud_x/100)), 
                      (0, 400, 1500, 400))
                      
    else:
        rect(screen, (53 + int(13*(cloud_x-100)/100),
                      152 + int(37*(cloud_x-100)/100),
                      68 + int(16*(cloud_x-100)/100)),
                      (0, 400, 1500, 400))

#drawing function

def function(k):
        
        """
        Если облако имеет координату х от 0 до 200, то изменяется цвет неба и поля.
        k - номер итерации.
        """

        big_cloud_x = 1200 + k - 1500 * ((1200 + k) // 1500)
        top_cloud_x = 620 + 3*k - 1500 * (( 620 + 3*k) // 1500)
        screen = pygame.display.set_mode((1500, 800))


        if top_cloud_x > 200 and big_cloud_x > 200:
            screen.fill([135, 206, 250])
            rect(screen, (66, 189, 84), (0, 400, 1500, 400))
        
        elif top_cloud_x > 200 and big_cloud_x <= 200:
            sky_color(big_cloud_x)
            field_color(big_cloud_x)

        elif top_cloud_x <= 200 and big_cloud_x > 200:
            sky_color(top_cloud_x)
            field_color(top_cloud_x)

        else:
            if abs(top_cloud_x - 100) > abs(big_cloud_x - 100):
                sky_color(big_cloud_x)
                field_color(big_cloud_x)
        
            else:
                sky_color(top_cloud_x)
                field_color(top_cloud_x)

        house(200, 450, 0.8)
        tree(650, 450, 0.7)
        house(900, 430, 0.5)
        tree(1200, 430, 0.5)
        sun(100, 100, 1)
        cloud(800+2*k - 1500*((800+2*k)//1500), 250, 0.4)
        cloud(big_cloud_x, 150, 0.5)    
        cloud(top_cloud_x, 100, 0.35) 

    
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    function(i)
    i+=1  
    pygame.display.update()

pygame.quit()

