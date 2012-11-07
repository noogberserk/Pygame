import random, pygame, sys, time
from pygame.locals import *


FPS = 2
PIXELSIZE = 20
X_SIZE = 10
Y_SIZE = 20
WINDOWWIDTH = X_SIZE * PIXELSIZE
WINDOWHEIGHT = Y_SIZE * PIXELSIZE
DOWNSPEED = 500

DRAWING_GRID = 0
ACTIVE_GRID = 1
RECTANGLE_GRID = 2
COLOR_GRID = 3


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


#SHAPES
TETRIMINOES = [['I',CYAN],['O',YELLOW],['T',PURPLE],['S',GREEN],['Z',RED],['J',BLUE],['L',ORANGE]]



def main():
    global FPSCLOCK, DISPLAYSURF, BOUNDING_BOX
    
    BOUNDING_BOX = [0,0]
    
    pygame.init()
    pygame.display.set_caption('TD')
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    
    
    splashScreen()
    
    #### INICIALIZADA LA GRILLA VACIA
    mainGrid = initGrid()
    
    
    # INICIALIZO UN TETRIMINO AL AZAR EN LA GRILLA DE TILES ACTIVOS
    setActiveTiles(mainGrid)
    pygame.time.set_timer(USEREVENT, DOWNSPEED)
    
    
    
    
    while True:
        pressedKeys = pygame.key.get_pressed()
        #isMovingFast = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_LEFT or event.key == K_RIGHT):
                setNewPosition(mainGrid,event.key)
                
            if event.type == KEYUP and (event.key == K_LEFT or event.key == K_RIGHT):
                #SI SE LEVANTA LA TECLA SE RESETEA EL FLAG PARA MOVER LAS FICHAS CON LAS TECLAS PRESIONADAS
                print True
            if event.type == KEYUP and event.key == K_RETURN:
                printGrid(mainGrid,DRAWING_GRID)
                #printGrid(mainGrid,ACTIVE_GRID)
            if event.type == USEREVENT:
                timeMovement(mainGrid)
            if event.type == KEYUP and event.key == K_UP:
                rotatingTile(mainGrid)
            
        if pressedKeys[K_DOWN] == True:    
            timeMovement(mainGrid)
#        elif pressedKeys[K_LEFT]  and isMovingFast:
#            setNewPosition(mainGrid,K_LEFT)
#        elif pressedKeys[K_RIGHT] and isMovingFast: 
#            setNewPosition(mainGrid,K_RIGHT)
                
        # TRASLADO LOS TILES ACTIVOS A LA GRILLA DE DIBUJO
        setActiveToDrawing(mainGrid)
        #printGrid(mainGrid,COLOR_GRID)
        
        
        #setNextStep(mainGrid)
        
        
        drawGrid(mainGrid)
        FPSCLOCK.tick(20)
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
    pygame.display.update()
    
def initGrid():
    grid = []
    for x in range(X_SIZE):
        column = []
        for y in range(Y_SIZE):
            coord = []
            coord.append(False)    
            coord.append(False)
            coord.append(pygame.Rect(x*PIXELSIZE,y*PIXELSIZE,PIXELSIZE,PIXELSIZE)) 
            coord.append(BLACK)
            column.append(coord) 
        grid.append(column)
        #print column
    return grid

def printGrid(grid,pos):
    print "grid ",pos
    result = ''
    for y in range(Y_SIZE):
        for x in range(X_SIZE):
            result += str(grid[x][y][pos])+' '
        print result
        result = ''
    print
    
def drawGrid(grid):
    DISPLAYSURF.fill(BLACK)
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y][DRAWING_GRID] == True:
                pygame.draw.rect(DISPLAYSURF,WHITE,grid[x][y][2])
    pygame.draw.rect(DISPLAYSURF,CYAN,(BOUNDING_BOX[0]*PIXELSIZE,BOUNDING_BOX[1]*PIXELSIZE,PIXELSIZE,PIXELSIZE))
    pygame.display.update()
        
def setRandomTrue(grid):
    grid[random.randrange(X_SIZE)][random.randrange(Y_SIZE)][0] = True

def getRandomTetrimino(TETRIMINOES):
    tetrimino = random.randrange(len(TETRIMINOES)-1)
    return TETRIMINOES[tetrimino][DRAWING_GRID],TETRIMINOES[tetrimino][ACTIVE_GRID]

def setActiveTiles(grid):
    shape,color = getRandomTetrimino(TETRIMINOES)
    #shape = 'I'
    if shape == 'I':
        grid[4][1][ACTIVE_GRID] = True
        grid[4][2][ACTIVE_GRID] = True
        grid[4][3][ACTIVE_GRID] = True
        grid[4][4][ACTIVE_GRID] = True
        grid[4][1][COLOR_GRID] = color
        grid[4][2][3] = color
        grid[4][3][3] = color
        grid[4][4][3] = color
    elif shape == 'O':
        grid[4][2][ACTIVE_GRID] = True
        grid[4][3][ACTIVE_GRID] = True
        grid[5][2][ACTIVE_GRID] = True
        grid[5][3][ACTIVE_GRID] = True
        grid[4][2][3] = color
        grid[4][3][3] = color
        grid[5][2][3] = color
        grid[5][3][3] = color
    elif shape == 'T':
        grid[3][3][ACTIVE_GRID] = True
        grid[4][2][ACTIVE_GRID] = True
        grid[4][3][ACTIVE_GRID] = True
        grid[5][3][ACTIVE_GRID] = True
        grid[3][3][3] = color
        grid[4][2][3] = color
        grid[4][3][3] = color
        grid[5][3][3] = color
    elif shape == 'S':
        grid[3][3][ACTIVE_GRID] = True
        grid[4][3][ACTIVE_GRID] = True
        grid[4][2][ACTIVE_GRID] = True
        grid[5][2][ACTIVE_GRID] = True
        grid[3][3][3] = color
        grid[4][3][3] = color
        grid[4][2][3] = color
        grid[5][2][3] = color
    elif shape == 'Z':
        grid[3][2][ACTIVE_GRID] = True
        grid[4][2][ACTIVE_GRID] = True
        grid[4][3][ACTIVE_GRID] = True
        grid[5][3][ACTIVE_GRID] = True
        grid[3][2][3] = color
        grid[4][2][3] = color
        grid[4][3][3] = color
        grid[5][3][3] = color
    elif shape == 'J':
        grid[3][2][ACTIVE_GRID] = True
        grid[3][3][ACTIVE_GRID] = True
        grid[4][3][ACTIVE_GRID] = True
        grid[5][3][ACTIVE_GRID] = True
        grid[3][4][3] = color
        grid[4][2][3] = color
        grid[4][3][3] = color
        grid[4][4][3] = color
    elif shape == 'L':
        grid[5][2][ACTIVE_GRID] = True
        grid[3][3][ACTIVE_GRID] = True
        grid[4][3][ACTIVE_GRID] = True
        grid[5][3][ACTIVE_GRID] = True
        grid[5][4][3] = color
        grid[4][2][3] = color
        grid[4][3][3] = color
        grid[4][4][3] = color
    BOUNDING_BOX[0] = 4
    BOUNDING_BOX[1] = 3
    
def setActiveToDrawing(grid):
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y][ACTIVE_GRID] == True:
                grid[x][y][DRAWING_GRID] = True
                
def cleanGrid(grid,pos):
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y][pos] == True:
                grid[x][y][pos] = False

def getBigger(positions,x):
    result = 0
    for i in positions:
        if i[x] > result:
            result = i[x]
    return result

def getSmaller(positions,coord):
    result = Y_SIZE
    for i in positions:
        if i[coord] < result:
            result = i[coord]
    return result

def setNewPosition(grid,key):
    positions = []
    #GUARDO LAS 4 COORDENADAS DONDE ESTA LA PIEZA ANTES DEL MOVIMIENTOS.
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y][ACTIVE_GRID] == True:
                positions.append([x,y])
                #BORRO LA PIEZA DE LA GRILLA DE DIBUJO
                grid[x][y][DRAWING_GRID] = False
    #BORRO LA PIEZA
    cleanGrid(grid,1)
     
    ##### CHECKEO DE POSICION ####   
    if key == K_RIGHT:
        far_x = getBigger(positions,DRAWING_GRID)
        ###CHECKEO QUE LA POSICION DE LA PIEZA ESTE EN EL LIMITE. ### NI A LA IZQUIERDA DE UN TILE YA COLOCADO
        #print "RIGHT: ",far_x,"| X SIZE: ",X_SIZE-2
        if far_x > X_SIZE-2:
            #PIEZA EN EL LIMITE. VUELVO LA PIEZA A LA POSICION ANTERIOR
            for coord in positions:
                grid[coord[0]][coord[1]][ACTIVE_GRID] = True
            return
        elif collitionRight(positions,grid):
            for coord in positions:
                #COLISION. VUELVO LA PIEZA A LA POSICION ANTERIOR
                grid[coord[0]][coord[1]][ACTIVE_GRID] = True
            return
        else:
            #PIEZA LEJOS DEL LIMITE. LA MUEVO HACIA LA DERECHA
            for coord in positions:
                grid[coord[0]+1][coord[1]][ACTIVE_GRID] = True
                #Y ACOMPANIO CON EL BOUNDING BOX
            BOUNDING_BOX[0] += 1
                
    elif key == K_LEFT:
        closer_x = getSmaller(positions,DRAWING_GRID)
        #CHECKEO QUE LA POSICION DE LA PIEZA ESTE EN EL LIMITE.
        #print "RIGHT: ",closer_x,"| comparacion: ",1
        if closer_x < 1:
            #PIEZA EN EL LIMITE. VUELVO LA PIEZA A LA POSICION ANTERIOR
            for coord in positions:
                grid[coord[0]][coord[1]][ACTIVE_GRID] = True
            return
        elif collitionLeft(positions,grid):
            for coord in positions:
                grid[coord[0]][coord[1]][ACTIVE_GRID] = True
            return
        else:
            #PIEZA LEJOS DEL LIMITE. LA MUEVO HACIA LA IZQUIERDA
            for coord in positions:
                grid[coord[0]-1][coord[1]][ACTIVE_GRID] = True 
            
            BOUNDING_BOX[0] -= 1
def checkGameOver(grid):
    for x in range(X_SIZE):
        if grid[x][2][DRAWING_GRID] == True:
            return True
    return False
    
def timeMovement(grid):
    #GUARDO LA POSICION DE LA PIEZA ANTES DE MOVERLA HACIA DONDE CRECE EL EJE Y.
    positions = []
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y][ACTIVE_GRID] == True:
                positions.append([x,y])
                #BORRO LA POSICION DE LA GRILLA DE DIBUJO
                grid[x][y][DRAWING_GRID] = False
    
    #CHECKEO QUE LA PIEZA NO ESTE EN EL FONDO DE LA GRILLA
    if isAtBottom(grid):
        print "is at bottom!"
        #SI ES ASI GUARDO LA PIEZA EN LA GRILLA DE DIBUJO
        setActiveToDrawing(grid)
        #BORRO LA GRILLA ACTIVA
        cleanGrid(grid,1)
        #CHECKEO SI EXISTE UNA LINEA
        checkLine(grid)
        #CHECKEO SI HAY PIEZAS COLOCADAS A LA ALTURA DE LA SALIDA (AKA GAME OVER)
        if checkGameOver(grid):
            gameOverFont = pygame.font.Font('freesansbold.ttf',30)
            gameOverSurface = gameOverFont.render('GAME OVER',True,RED)
            gameOverRect = gameOverSurface.get_rect()
            gameOverRect.center = (X_SIZE*PIXELSIZE/2,Y_SIZE*PIXELSIZE/2)
            DISPLAYSURF.blit(gameOverSurface,gameOverRect)
            pygame.display.update()
            time.sleep(2)
            cleanGrid(grid,DRAWING_GRID)
        #E INICIALIZO OTRA PIEZA RANDOM
        setActiveTiles(grid)
        return
    else:
        #EN CASO DE QUE NO SEA EL FONDO DE LA GRILLA AVANZO UN CASILLERO EN EL EJE Y.
        cleanGrid(grid,ACTIVE_GRID)
        for coord in positions:
            grid[coord[0]][coord[1]+1][ACTIVE_GRID] = True
            #Y AHORA ACOMPANIO EL MOVIMIENTO CON LA BOUNDING BOX
            
        BOUNDING_BOX[1] += 1 
    
def isAtBottom(grid):
    positions = []
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y][ACTIVE_GRID] == True:
                positions.append([x,y])
                
    bigger_y = getBigger(positions,ACTIVE_GRID)
    if bigger_y >= Y_SIZE-1:
        return True
    else:
        for coord in positions:
            if grid[coord[0]][coord[1]+1][DRAWING_GRID] == True:
                return True
    return False
                 
def collitionRight(positions,grid):
    for coord in positions:
        if grid[coord[0]+1][coord[1]][DRAWING_GRID] == True:
            #print "COLLISION!"
            return True
    return False
    
def collitionLeft(positions,grid):
    for coord in positions:
        if grid[coord[0]-1][coord[1]][DRAWING_GRID] == True:
            #print "COLLISION!"
            return True
    return False
    #time.sleep(1)

def checkLine(grid):
    for y in range(Y_SIZE):
        row = []
        for x in range(X_SIZE):
            row.append(grid[x][y][DRAWING_GRID])
        #CHECKEO EN CADA FILA SI HAY LINEA
        if isLine(row):
            deleteLine(grid,y)
                    
def isLine(row):
    for i in row:
        if i == False:
            return False
    return True

def deleteLine(grid,deleting_y):
    previous_grid = copyGrid(grid,DRAWING_GRID)

    for y in range(Y_SIZE):
        for x in range(X_SIZE):
            if y < deleting_y:
                grid[x][y+1][DRAWING_GRID] = previous_grid[x][y]
            else:
                return
            
def copyGrid(grid,pos):
    result = []
    for x in range(X_SIZE):
        row = []
        for y in range(Y_SIZE):
            row.append(grid[x][y][pos])
        result.append(row)
    return result


def isOTetrimino(positions):
    if positions[0][0] == positions[1][0] and positions [2][0] == positions[3][0]:
        if positions[0][1] == positions[2][1] and positions[1][1] == positions[3][1]:
            return True
    
def isITetrimino(positions):
    x_count = 0
    y_count = 0

    for coord in positions:
        if positions[0][0] == coord[0]:
            x_count+=1
            if x_count >= 4:
                return True
        if positions[0][1] == coord[1]:
            y_count+=1
            if y_count >= 4:
                return True
        

def rotatingTile(grid):
    positions = []
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if grid[x][y][ACTIVE_GRID] == True:
                #GUARDO LAS POSICIONES EN LA QUE HAY TILES ACTIVOS
                positions.append([x,y])
                #Y LAS BORRO DE LA GRILLA DE DIBUJO
                grid[x][y][DRAWING_GRID] = False

    #CHECK IF THIS IS AN O TETRIMINO. NO NEED TO ROTATE
    if isOTetrimino(positions):
        return
       
    
    #BORRO LA GRILLA ACTIVA PARA HACER LUGAR PARA EL MOVIMIENTO
    cleanGrid(grid,ACTIVE_GRID)
    
    #BUSCO QUE LA PIEZA NO ESTE EN EL LIMITE DERECHO DE LA PANTALLA
    if BOUNDING_BOX[0] >= X_SIZE-1:
        #MUEVO LA PIEZA y SU EJE UN CASILLERO A LA IZQUIERDA (SOBRE EL EJE X)
        BOUNDING_BOX[0] -= 1
        for i in positions:
            i[0] -= 1 
    #BUSCO QUE NO ESTE EN EL LIMITE IZQUIERDO
    elif BOUNDING_BOX[0] <= 0:
        #MUEVO LA PIEZA HACIA LA DERECHA (SOBRE EL EJE X) UN CASILLERO
        BOUNDING_BOX[0] +=1
        for i in positions:
            i[0] +=1
    
    
    #SI LA PIEZA ES UNA I y ESTA EN EL X=0 o X=1 NECESITO MOVERLA PARA PODER ROTARLA
    if isITetrimino(positions) and BOUNDING_BOX[0] <= 1:
        #MUEVO LA PIEZA HACIA LA POSICION X=2
        BOUNDING_BOX[0] = 2
        for i in positions:
            i[0] = 2
            
            
    #GUARDO EL X, Y MAS CHICOS PARA INICIALIZAR EL BOUNDING BOX
    rotate_x = BOUNDING_BOX[0]-1
    rotate_y = BOUNDING_BOX[1]-1
    for coord in positions:
        #RESTO EL BOUNDING BOX PARA MOVER LA GRILLA AL 0,0
        coord[0] -= rotate_x
        coord[1] -= rotate_y
        #TRANSPONGO (SI ES QUE ES LA PALABRA), LA GRILLA. X -> Y and Y->X
        coord[0],coord[1] = coord[1],coord[0]
        #ESPEJO LA GRILLA ROTADA
        if coord[0] == 0:
            coord[0] = 2
        elif coord[0] == 2:
            coord[0] = 0
        #VUELVO A SUMARLE EL X e Y QUE LE RESTE PARA ROTAR LA GRILLA
        coord[0] += rotate_x
        coord[1] += rotate_y        
        #DEVUELVO LA PIEZA A SU POSICION ORIGINAL SOBRE LA GRILLA ACTIVA
        grid[coord[0]][coord[1]][ACTIVE_GRID] = True
         

main()