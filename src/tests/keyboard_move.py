import random, pygame, sys, time
from pygame.locals import *


FPS = 2
PIXELSIZE = 20
X_SIZE = 10
Y_SIZE = 22
WINDOWWIDTH = X_SIZE * PIXELSIZE
WINDOWHEIGHT = Y_SIZE * PIXELSIZE


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
    global FPSCLOCK, DISPLAYSURF
    x_mouse = y_mouse = 0
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('TD')
    
    splashScreen()
    pygame.display.update()
    
    mainBooleanGrid,mainRectArray = getMainGrid()
    x_coord, y_coord = getSquarePosition(mainBooleanGrid)
    
    while True:            
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
                
            if event.type == KEYUP:
                changeSquarePosition(mainBooleanGrid,event.key)
            
                    
                    
        DISPLAYSURF.fill(BLACK)
        printGrid(mainBooleanGrid)  
        #randomizeGrid(mainBooleanGrid)  
        x_coord, y_coord = getSquarePosition(mainBooleanGrid)
        pygame.draw.rect(DISPLAYSURF,WHITE,mainRectArray[x_coord][y_coord])
        pygame.display.update()
        
        FPSCLOCK.tick(60)
        
################ END OF MAIN LOOP ##################
    
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
    
def getMainGrid():
    gridBoolean = []
    gridRect = []
    for x in range(X_SIZE):
        columnBoolean = []
        columnRect = []
        for y in range(Y_SIZE):
            columnBoolean.append((x,y))
            columnRect.append(pygame.Rect(x*PIXELSIZE,y*PIXELSIZE,PIXELSIZE,PIXELSIZE))
        gridBoolean.append(columnBoolean)
        gridRect.append(columnRect)
    setRandomTrue(gridBoolean)
    return gridBoolean,gridRect
    
def getSquarePosition(grid):
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y] == True:
                return  x,y
    return 0,0

def printGrid(grid):
    result = ''
    for y in range(Y_SIZE):
        for x in range(X_SIZE):
            result += str(grid[x][y])+' '
        print result
        result = ''
    print
        
def setRandomTrue(grid):
    grid[random.randrange(X_SIZE)][random.randrange(Y_SIZE)] = True
        
def randomizeGrid(grid):
    x,y = getSquarePosition(grid)
    grid [x][y] = (x,y)
    setRandomTrue(grid)
    
def changeSquarePosition(grid, key):
    x, y = getSquarePosition(grid) 
    
    if key == K_UP:
        if y <= 0:
            
            return
        else:
            grid[x][y] = (x,y)
            grid[x][y-1] = True
    elif key == K_DOWN:
        if y >= Y_SIZE-1:
            return
        else:
            grid[x][y] = (x,y)
            grid[x][y+1] = True
    elif key == K_RIGHT:
        if x >= X_SIZE-1:
            return
        else:
            grid[x][y] = (x,y)
            grid[x+1][y] = True
    elif key == K_LEFT:
        if x <= 0:
            return
        else:
            grid[x][y] = (x,y)
            grid[x-1][y] = True
            
main()
