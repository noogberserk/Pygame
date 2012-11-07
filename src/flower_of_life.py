import pygame, sys, math
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
RADIUS = 45

#sixty_degrees = 60 * math.pi / 180
#
#CENTER = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
#SECOND = (WINDOWWIDTH/2,WINDOWHEIGHT/2-RADIUS)
#VESICA = (WINDOWWIDTH/2,WINDOWHEIGHT/2-(RADIUS/2))
#
#next_point1 = math.tan(sixty_degrees)*(CENTER[1]-VESICA[1])
#
#THIRD = (WINDOWWIDTH/2+int(next_point1),VESICA[1])
#FOURTH = (THIRD[0],THIRD[1]+RADIUS)
#FIFTH = (WINDOWWIDTH/2,WINDOWHEIGHT/2+RADIUS)
#SIXTH = (WINDOWWIDTH/2-int(next_point1),FOURTH[1])
#SEVENTH = (SIXTH[0],THIRD[1])
#
#SEED = [CENTER,SECOND,THIRD,FOURTH,FIFTH,SIXTH,SEVENTH]
#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
GREEN =         (  0, 255,   0)

def main():
    global DISPLAYSURF, FPSCLOCK
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    STATE = 0
    
    splashScreen()
    SEED = fillSeed(WINDOWWIDTH/2,WINDOWHEIGHT/2)
    BRANCHES = fillBranches(SEED)
    TREE = []
    for i in BRANCHES:
        TREE.append(fillBranches(i))
    

    while True:
        DISPLAYSURF.fill(BLACK)
        for event in pygame.event.get():
            if event.type == KEYUP and event.key == K_UP:
                STATE += 1
            if event.type == KEYUP and event.key == K_DOWN:
                STATE -= 1
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        if STATE > 0:
            drawFlower(STATE,SEED)
            for branch in BRANCHES:
                drawFlower(STATE,branch)
            for j in TREE:
                for f in j:
                    drawFlower(STATE,f)
                    pygame.draw.circle(DISPLAYSURF,WHITE,f[0],RADIUS,1)
        
#        pygame.draw.circle(DISPLAYSURF,WHITE,CENTER,1,1)
#        pygame.draw.circle(DISPLAYSURF,WHITE,THIRD,1,1)
#        pygame.draw.circle(DISPLAYSURF,GREEN,VESICA,RADIUS/2,1)
#        pygame.draw.lines(DISPLAYSURF,WHITE,True,SEED)
#        pygame.draw.line(DISPLAYSURF,WHITE,CENTER,SECOND)
#        pygame.draw.line(DISPLAYSURF,WHITE,CENTER,THIRD)
#        pygame.draw.line(DISPLAYSURF,WHITE,CENTER,THIRD)
#        pygame.draw.line(DISPLAYSURF,WHITE,THIRD,FOURTH)
        pygame.display.update()
        
        
def drawFlower(STATE,SEED):
    for i in range(STATE):
        if i < len(SEED):
            pygame.draw.circle(DISPLAYSURF,GREEN,SEED[i],RADIUS,1)
        
#        if i == 0:
#            pygame.draw.line(DISPLAYSURF,WHITE,SEED[1],SEED[6])
#        elif i < len(SEED):
#            pygame.draw.line(DISPLAYSURF,WHITE,SEED[i],SEED[i-1])

def fillSeed(x,y):
    CENTER = (x,y)
    SECOND = (CENTER[0],CENTER[1]-RADIUS)
    sixty_degrees = 60 * math.pi / 180
    next_point = math.tan(sixty_degrees)*(RADIUS/2)
    THIRD = (x+int(next_point),y-RADIUS/2)
    FOURTH = (THIRD[0],THIRD[1]+RADIUS)
    FIFTH = (x,y+RADIUS)
    SIXTH = (x-int(next_point),FOURTH[1])
    SEVENTH = (SIXTH[0],THIRD[1])
    SEED = [CENTER,SECOND,THIRD,FOURTH,FIFTH,SIXTH,SEVENTH]
    return SEED

def fillBranches(SEED):
    BRANCHES = []
    for branch in SEED:
        BRANCHES.append(fillSeed(branch[0],branch[1]))
    return BRANCHES












def splashScreen():
    splashFont = pygame.font.Font('freesansbold.ttf', 16)
    splashFontSurface = splashFont.render('Press Enter to begin',True,WHITE)
    splashSurfaceRect = splashFontSurface.get_rect()
    splashSurfaceRect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
    while True:
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(splashFontSurface,splashSurfaceRect)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYUP and event.key == 13:
                return
    pygame.display.update()
    
    
main()