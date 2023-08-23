import random

def generate(dimx,dimy):
    global wall_counter
    x,y = random.randint(0,dimx-1),random.randint(0,dimy-1)
    visited=[(x,y)]
    carvedList=[(x,y)]
    walled=[]
    wall_counter = 0

    Map = {}
    for y in range(dimy):
        for x in range(dimx):
            Map[(x,y)] = [],[]


    for y in range(dimy):
        for x in range(dimx):
            if -1 < x-1 < dimx:
                Map[(x,y)][0].append((x-1,y))
            if -1 < x+1 < dimx:
                Map[(x,y)][0].append((x+1,y))
            if -1 < y-1 < dimy:
                Map[(x,y)][0].append((x,y-1))
            if -1 < y+1 < dimy:
                Map[(x,y)][0].append((x,y+1))

    def move(x,y,visited,carvedList,walled):
        global wall_counter
        moved = False
        positions = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        while not moved:

            a = random.choice(positions)
            positions.remove(a)
            if -1 < a[0] < dimx and -1 < a[1] < dimy:

                if not (a[0],a[1]) in visited:
                    x,y = a[0],a[1]
                    visited.append((x,y))
                    carvedList.append((x,y))
                    moved = True
                    return x,y

            if positions == []:
                x,y = carvedList[-1]
                carvedList.pop()
                moved = True
                walled.append((x,y))
                if -1 < y-1 < dimy:
                    if (x,y-1) in visited and (x,y-1) != carvedList[-1] and not (x,y-1) in walled and len(carvedList) > 2:
                        if random.randint(1,3) != 1:
                            wall_counter += 1
                            try:
                                Map[(x,y-1)][0].remove((x,y))
                                Map[(x,y)][0].remove((x,y-1))
                            except:
                                'a'
                if -1 < y+1 < dimy:
                    if (x,y+1) in visited and (x,y+1) != carvedList[-1] and not (x,y+1) in walled and len(carvedList) > 2:
                        if random.randint(1,3) != 1:
                            wall_counter += 1
                            try:
                                Map[(x,y+1)][0].remove((x,y))
                                Map[(x,y)][0].remove((x,y+1))
                            except:
                                'a'

                if -1 < x+1 < dimy:
                    if (x+1,y) in visited and (x+1,y) != carvedList[-1] and not (x+1,y) in walled and len(carvedList) > 2:
                        if random.randint(1,3) != 1:
                            wall_counter += 1
                            try:
                                Map[(x+1,y)].remove((x,y))
                                Map[(x,y)].remove((x+1,y))
                            except:
                                'a'


                if -1 < x-1 < dimy:
                    if (x-1,y) in visited and (x-1,y) != carvedList[-1] and not (x-1,y) in walled and len(carvedList) > 2:
                        if random.randint(1,3) != 1:
                            wall_counter += 1
                            try:
                                Map[(x-1,y)][0].remove((x,y))
                                Map[(x,y)][0].remove((x-1,y))
                            except:
                                'a'
                return x,y
    run=True
    start = True
    while run:

        while len(walled) < dimx*dimy-1:
            x,y = move(x,y,visited,carvedList,walled)
            start = False

        if wall_counter < dimx*dimy * 30/100:
            x,y = random.randint(0,dimx-1),random.randint(0,dimy-1)
            visited=[(x,y)]
            carvedList=[(x,y)]
            walled=[]
            wall_counter = 0
            start = True
        else:
            run = False
    return Map

