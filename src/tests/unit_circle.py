import pygame, sys, math,time,random
from pygame.locals import *

WINDOWWIDTH,WINDOWHEIGHT = 640,480

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
    global DISPLAYSURF
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    splashScreen()
    angle = 0
    
    x_movement = 0
    y_movement = 0
    
    x_cursor = WINDOWWIDTH/2
    y_cursor = WINDOWHEIGHT/2
    
    random_x = random.randrange(639)
    random_y = random.randrange(439)
    
    DISPLAYSURF.fill(BLACK)     
    while True:
        #DISPLAYSURF.fill(BLACK)  
#        if x_movement >=random_x:
#            x_movement = 0
#            random_x = random.randrange(639)
#        elif y_movement >=random_y:
#            y_movement = 0
#            random_y = random.randrange(439)
            
               
        angle+=1*math.pi/180
        if angle % 90*math.pi/180:
            angle += 1*math.pi/180
        #print "angle: ",angle,"            angle (degrees): ",angle*180/math.pi
        print 
        x_movement += 1 
        y_movement +=1
        if x_movement == 639:
            x_movement = 0
        pixObj = pygame.PixelArray(DISPLAYSURF)
        #print "cos: ",int(math.cos(angle))+x_movement
        #print "sin: ",math.sin(angle)
#        pixObj[x_movement][int(math.sin(angle)*30)+y_cursor] = GREEN
#        pixObj[y_movement][int(math.cos(angle)*30)+x_cursor] = GREEN
#        pixObj[int(math.cos(angle)*30)+320][int(math.sin(angle)*30)+240] = WHITE
            
        tangente = int(math.tan(angle))
        
        print "tan: ",tangente," | angle",angle#*180/math.pi 
        if angle != 90 and angle!=180 and angle != 270 and angle!=360:
            pixObj[x_movement][tangente+60] = CYAN
        
        del pixObj
        #pygame.draw.line(DISPLAYSURF,WHITE,(320,240),(int(math.cos(angle)*320)+320,int(math.sin(angle)*240)+240))
        
        
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP and event.key == K_RIGHT:
                x_cursor +=1
            elif event.type == KEYUP and event.key == K_LEFT:
                y_cursor+=1
            elif event.type == KEYUP and event.key == K_RETURN:
                random_x = random.randrange(639)
                random_y = random.randrange(439)
            elif event.type == KEYUP and event.key == K_SPACE:
                DISPLAYSURF.fill(BLACK)
        pygame.display.update()
        time.sleep(0.1)
        
    
    
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