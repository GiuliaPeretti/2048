import pygame

SCREEN_WIDTH,SCREEN_HEIGHT = 800,600
BLACK=(0,0,0)
LIGHT_GRAY=(240,240,240)
GRAY=(200,200,200)
DARK_GRAY=(150,150,150)
PINK=(255, 179, 217)
RED=(255,0,0)
BROWN=(100,50,0)
WHITE=(255,255,255)
BLUE=(0,0,255)

BACKGROUND_COLOR = BLACK
#               2,              4,              8,              16,                 32,             64,          128,           256,            512,        1024,       2048
COLORS=[{'n':0,'color':(0,0,0)},
        {'n':2,'color':(250, 230, 47)},
        {'n':4,'color':(255, 185, 23)},
        {'n':8,'color': (255, 143, 23)},
        {'n':16,'color':(255, 100, 23)},
        {'n':32,'color':(255, 62, 23)},
        {'n':64,'color':(255, 23, 73)},
        {'n':128,'color':(255, 23, 131)}, 
        {'n':256,'color':(255, 23, 243)},
        {'n':512,'color':(170, 23, 255)},
        {'n':1024,'color':(69, 23, 255)},
        {'n':2048,'color':(23, 185, 255)}]

flags=(pygame.HWSURFACE | pygame.DOUBLEBUF)
