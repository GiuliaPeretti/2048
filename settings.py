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
#               2,              4,              8,              16,         32,             64,          128,           256,            512,        1024,       2048
COLORS=[(0,0,0),(252, 248, 154),(255, 223, 94), (255, 192, 74),(242, 171, 39),(242, 144, 39),(245, 121, 27),(227, 84, 27), (227, 40, 11),(227, 11, 94),(227, 11, 202),(155, 11, 227)]

flags=(pygame.HWSURFACE | pygame.DOUBLEBUF)
