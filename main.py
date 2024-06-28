import pygame
from settings import *
import random
import time
import math


def draw_background():
    screen.fill(BACKGROUND_COLOR)

def gen_buttons():
    x,y,w,h=640,20,100,30
    buttons=[]
    for i in range (1,5):
        buttons.append({'name': 'Level '+str(i), 'coordinates': (x,y,w,h)})
        y=y+h+10
    buttons.append({'name': 'Play', 'coordinates': (x,y,w,h)})
    return(buttons)


def draw_buttons():   
    for b in buttons[:len(buttons)]:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+17,b['coordinates'][1]+3))
    
    if selected!=-1:
        pygame.draw.rect(screen, PINK, buttons[selected]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons[selected]['coordinates'], 3)
        text=font.render(buttons[selected]['name'], True, BLACK)
        screen.blit(text, (buttons[selected]['coordinates'][0]+17,buttons[selected]['coordinates'][1]+3))

    pygame.draw.rect(screen, GRAY, buttons[-1]['coordinates'])
    pygame.draw.rect(screen, BLACK,  buttons[-1]['coordinates'], 3)
    text=font.render( buttons[-1]['name'], True, BLACK)
    screen.blit(text, ( buttons[-1]['coordinates'][0]+30, buttons[-1]['coordinates'][1]+3))
    
    pygame.display.flip()
    
def init_cell(size):
    cells=[]
    for i in range (size):
        t=[]
        for j in range(size):
            t.append(0)
        cells.append(t)
    return(cells)

def draw_grid():
    pygame.draw.rect(screen, BACKGROUND_COLOR, (0,0,600,600))
    for i in range (20,581,cell_width):
        pygame.draw.line(screen, WHITE, (i,20),(i,580), 2)
        pygame.draw.line(screen, WHITE, (20,i),(580,i), 2)

    for i in range(0,len(COLORS)):
        pygame.draw.rect(screen, COLORS[i], (10*i,0,10,10))

def draw_square(row,col):
    x=(col*cell_width)+20+10
    y=(row*cell_width)+20+10
    w=cell_width-18
    pygame.draw.rect(screen, COLORS[int(math.sqrt(cells[row][col]))], (x,y,w,w))

def start_the_game():
    for i in range(3):
        row=random.randint(0,size-1)
        col=random.randint(0,size-1)
        cells[row][col]=2
    update_grid()


def update_grid():
    for row in range(0,size):
        for col in range(0,size):
            draw_square(row, col)

def move_up():
    for col in range(size-1):
        for row in range(size-1,-1,-1):
            if(row-1>0 and (cells[row-1][col]==cells[row][col] or cells[row-1][col]==0)):
                cells[row-1][col]=cells[row-1][col]+cells[row][col]
                cells[row][col]=0
    update_grid()







def get_cell_size():
    match select_game:
        case 0:
            return(140, 560//140)
        case 1:
            return(112, 560//112)
        case 2:
            return(80, 560//80)
        case 3:
            return(70, 560//70)


if __name__=='__main__':

    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('2048♥')
    font = pygame.font.SysFont('arial', 20)

    #28, 40, 56, 80
    #20, 14, 10, 7

    selected=-1
    cell_width=560
    size=1
    selected_game=-1
    game_started=False
    grid=None
    draw_background()
    buttons=gen_buttons()
    draw_buttons()
    draw_grid()
    # number_player()



    run  = True

    number=0

    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                for i in range (len(buttons)):
                    if(x>=buttons[i]['coordinates'][0] and x<=buttons[i]['coordinates'][0]+buttons[i]['coordinates'][2] and y>=buttons[i]['coordinates'][1] and y<=buttons[i]['coordinates'][1]+buttons[i]['coordinates'][3]):
                        if(i<len(buttons)-1):
                            selected=i
                            if(not(game_started)):
                                select_game=selected
                            draw_buttons()
                            break
                        elif(i==4):
                            if(selected!=-1):
                                pygame.draw.rect(screen, BACKGROUND_COLOR, (640,490,100,100))   
                                select_game=selected
                                win=False
                                loose=False
                                game_started=True
                                cell_width, size=get_cell_size()
                                cells=init_cell(size)
                                draw_grid()
                                draw_buttons()
                                start_the_game()

                            break
                else:
                    selected=-1
                draw_buttons()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_UP:
                    print("up")
                    move_up()
                if event.key == pygame.K_RIGHT:
                    print("right")
                if event.key == pygame.K_DOWN:
                    print("down")
                if event.key == pygame.K_LEFT:
                    print("left")
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()