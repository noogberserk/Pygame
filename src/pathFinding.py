def g(x,y, parentX, parentY):
    if (abs(x - parentX) == 1 and abs(y - parentY)):
        result = 14;
    else:
        result = 10;

    haveParent = True;
    
    try:
        cost_list[parentX, parentY]["g"]
    except:
        haveParent = False;

    if haveParent:
        return cost_list[parentX, parentY]["g"] + result
    return result


def h(x,y, targetX, targetY):
    return 10 * (abs(x - targetX) + abs(y - targetY));


def findPath(cost_list, targetX, targetY):
    nextStep = cost_list[(targetX, targetY)]['parent'];
    print targetX, targetY, " | ", nextStep[0], nextStep[1];
    try:
        return findPath(cost_list, nextStep[0], nextStep[1]), nextStep[0], nextStep[1];
    except:
        return nextStep[0], nextStep[1];
    


myMap = [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,0,1],
         [0,0,9,0,0,1,9,1],
         [0,0,0,0,0,1,0,0],
         [0,0,0,0,0,1,0,0],
         [0,0,0,0,0,1,0,0]];

open_list = [[2,2]];
closed_list = [];
#parent:parent, f:int, g:int, h:int;
cost_list = {};

for i in myMap:
    print i;
print

def find(targetX, targetY):
    #Inicio con el primer parent.
    parentX = open_list[0][0];
    parentY = open_list[0][1];
    
    #For the loop
    finished = False;

    while not finished:
        
        #Fuerzo la busqueda de un menor dentro de cost_list
        lowest = 100000;
        
        #Recorro el diccionario "cost_list" buscando la entrada con menor costo de F.
        #Checkeo que tampoco este dentro de closed_list para que sea una posicion aun no recorrida.
        for entry in cost_list:
            if (lowest >= cost_list[entry]["f"]) and ([entry[0], entry[1]] in open_list):
                #Cuando lo encuentro lo guardo en parentX y parentY para utilizarlo en la busqueda.
                lowest = cost_list[entry]["f"];
                parentX = entry[0];
                parentY = entry[1];
                
        #Checkeo que la posicion que encontre sea la que estoy buscando
        if targetX == parentX and parentY == targetY:
            print "--------------- result --------------\n"
            for u in cost_list:
                print u, cost_list[u];
            #Y devuelvo una tupla loca creada por una funcion recursiva que busca en cost_list el parent del parent del parent, etc.
            return findPath(cost_list, targetX, targetY), (targetX, targetY);
        
        print  
        print "|-- current position x:", parentX, "y:", parentY, "content", myMap[parentY][parentX], " --|";
        print

        #Busco la posicion del XY actual en la lista abierta, para moverlo a la lista cerrada.
        count = 0;
        index = 0;
        for toRemove in open_list:
            if toRemove == [parentX, parentY]:
                index = count;
            count += 1;
        closed_list.append(open_list.pop(index));



        #Busco los 8 lugares adjacentes a la posicion actual.
        for x in range(parentX - 1, parentX + 2):
            for y in range(parentY - 1, parentY + 2):

                #Si esta dentro del rango del array...
                if (x > 0 and y > 0) and (y < len(myMap) and x < len(myMap[0])):
                    #Si no esta dentro de closed list y es caminable.
                    if (myMap[y][x] != 1) and (not [x,y] in closed_list):
                        if not [x,y] in open_list:
                            open_list.append([x, y]);
                            g_value = g(x, y, parentX, parentY);
                            h_value = h(x, y, targetX, targetY);
                            cost_list[(x,y)] = {"parent": (parentX, parentY), "f": g_value + h_value, "g": g_value, "h": h_value};
                            print "value:", myMap[y][x], "- x:", x, "| y:", y, "| F:", cost_list[(x,y)]["f"];
                        else:
                            if cost_list[(x,y)]["g"] >= g(x, y, parentX, parentY):
                                g_value = g(x, y, parentX, parentY);
                                h_value = h(x, y, targetX, targetY);
                                cost_list[(x,y)] = {"parent": (parentX, parentY), "f": g_value + h_value, "g": g_value, "h": h_value};
                                print "|cost changed| value:", myMap[y][x], "- x:", x, "| y:", y, "| F:", cost_list[(x,y)]["f"];
                                

        print "open list: ", open_list;
        #print "closed list", closed_list;
        print
        for y in cost_list:
            print y, cost_list[y];
        
        print '------------------------------------------------ \n||||||||||||||||||||||||||||||||||||||||||||||||\n------------------------------------------------'
        print

        if len(open_list) < 1:
            finished = True;


countY = 0;
countX = 0;

for p in myMap:
    for e in p:
        if e == 9:
            targetX, targetY = countX, countY;
        countX += 1;
    countX = 0;
    countY += 1;


print "the path to ", targetX, targetY, " is: ", find(targetX, targetY);

