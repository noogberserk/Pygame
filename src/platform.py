import random, pygame, sys, time, math
from pygame.locals import *

WINDOWWIDTH,WINDOWHEIGHT = 640,480
LINELENGTH = 100
# R G B
CYAN = ( 0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
GREEN = ( 0, 255, 0)
RED = (255, 0, 0)
BLUE = ( 0, 0, 255)
ORANGE = (255, 128, 0)

GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

def main():
    global FPSCLOCK, DISPLAYSURF, BOUNDING_BOX
    
    
    pygame.init()
    pygame.display.set_caption('PLATFORM')
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    
    splashScreen()
    charRect = initCharacter()
    
    angle = 0
    
    angleFont = pygame.font.Font('freesansbold.ttf', 16)
    angleFontSurface = angleFont.render(str(angle),True,GREEN)
    angleSurfaceRect = angleFontSurface.get_rect()
    angleSurfaceRect.center = (20,20)
    
    while True:
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(angleFontSurface,angleSurfaceRect)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYUP and event.key == K_RIGHT:
                charRect.center = (charRect.centerx+20,charRect.centery)
            elif event.type == KEYUP and event.key == K_LEFT:
                charRect.center = (charRect.centerx-20,charRect.centery)
                
        pygame.draw.rect(DISPLAYSURF,GREEN,charRect)
        
        
        adyacent, opposite = pygame.mouse.get_pos()
        opposite = charRect.centery - opposite
        adyacent -= charRect.centerx
        #print "ADYACENTE. X: ",adyacent, "           OPUESTO. Y: ",opposite,"          HIPOTENUSA: ",hipotenuse
        #print "ANGLE = ",angle,"*"
        angle = math.atan2(opposite,adyacent)*180/math.pi 
        
        top_angle = angle+30
        bottom_angle = angle-30
        #print top_angle,bottom_angle
        
        top_ady = 200 * math.cos(top_angle*math.pi/180)
        top_op = WINDOWHEIGHT - 200 * math.sin(top_angle*math.pi/180)
        
        bottom_ady = 200 * math.cos(bottom_angle*math.pi/180)
        bottom_op = WINDOWHEIGHT - 200 * math.sin(bottom_angle*math.pi/180)
        
        angleFontSurface = angleFont.render("Angle: "+str(angle)+"\ntop_angle: "+str(top_angle)+"\nbottom_angle: "+str(bottom_angle),True,GREEN)
        pygame.draw.line(DISPLAYSURF,NAVYBLUE,charRect.center,pygame.mouse.get_pos())
        pygame.draw.line(DISPLAYSURF,GREEN,charRect.center,(top_ady,top_op))
        pygame.draw.line(DISPLAYSURF,GREEN,charRect.center,(bottom_ady,bottom_op))
        pygame.display.update()
    
        



def initCharacter():
    return pygame.Rect(20,250,20,80)










def splashScreen():
    splashFont = pygame.font.Font('freesansbold.ttf', 16)
    splashFontSurface = splashFont.render('Press Enter to begin',True,GREEN)
    splashSurfaceRect = splashFontSurface.get_rect()
    splashSurfaceRect.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
    while True:
        DISPLAYSURF.fill(NAVYBLUE)
        DISPLAYSURF.blit(splashFontSurface,splashSurfaceRect)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYUP and event.key == 13:
                return
    
    

main()