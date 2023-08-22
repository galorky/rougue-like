import pygame,math,random,map_maker,maze_vizualiser

img_kresh = pygame.transform.scale(pygame.image.load('shrek.png'),(50,80))
img_kresh.set_colorkey((255,255,255))

img_ennemie = pygame.transform.scale(pygame.image.load('ennemie.png'),(50,80))
img_ennemie.set_colorkey((255,255,255))

xfen,yfen = 1600,900
dimx,dimy = 6,6
multix,multiy = xfen/dimx , yfen/dimy

maze = maze_vizualiser.show(dimx,dimy)

pygame.init()

fen = pygame.display.set_mode((xfen,yfen),pygame.FULLSCREEN)

class Joueur:
    def __init__(self):
        self.speed = 8
        self.x = xfen/2 - img_kresh.get_width()/2
        self.y = yfen/2 - img_kresh.get_height()/2
        self.dx,self.dy = 0,0

    def move(self):
        global loc
        keys = pygame.key.get_pressed()

        if not (keys[pygame.K_z] and keys[pygame.K_d] and keys[pygame.K_s] and keys[pygame.K_q]): #presse toutes les touches = pas bouger

            if sum(keys[i] for i in [pygame.K_q, pygame.K_d, pygame.K_z, pygame.K_s]) == 1: #presse que une touche parmi zqsd

                if keys[pygame.K_z] and not keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_q]:
                    self.y -= self.speed
                    self.dy = -self.speed
                    self.dx = 0

                elif not keys[pygame.K_z] and keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_q]:
                    self.x += self.speed
                    self.dx = self.speed
                    self.dy = 0

                elif not keys[pygame.K_z] and not keys[pygame.K_d] and keys[pygame.K_s] and not keys[pygame.K_q]:
                    self.y += self.speed
                    self.dy = self.speed
                    self.dx = 0

                elif not keys[pygame.K_z] and not keys[pygame.K_d] and not keys[pygame.K_s] and keys[pygame.K_q]:
                    self.x -= self.speed
                    self.dx = -self.speed
                    self.dy = 0


            else:
                if keys[pygame.K_z] and keys[pygame.K_d]:
                    self.x += self.speed * math.sqrt(2) / 2
                    self.y -= self.speed * math.sqrt(2) / 2
                    self.dx,self.dy = self.speed * math.sqrt(2) / 2 , -self.speed * math.sqrt(2) / 2

                elif keys[pygame.K_z] and keys[pygame.K_q]:
                    self.x -= self.speed * math.sqrt(2) / 2
                    self.y -= self.speed * math.sqrt(2) / 2
                    self.dx,self.dy = -self.speed * math.sqrt(2) / 2, -self.speed * math.sqrt(2) / 2

                elif keys[pygame.K_s] and keys[pygame.K_d]:
                    self.x += self.speed * math.sqrt(2) / 2
                    self.y += self.speed * math.sqrt(2) / 2
                    self.dx,self.dy = self.speed * math.sqrt(2) / 2, self.speed * math.sqrt(2) / 2


                elif keys[pygame.K_s] and keys[pygame.K_q]:
                    self.x -= self.speed * math.sqrt(2) / 2
                    self.y += self.speed * math.sqrt(2) / 2
                    self.dx,self.dy = -self.speed * math.sqrt(2) / 2,self.speed * math.sqrt(2) / 2

            if self.x > xfen - 15 - img_kresh.get_width() and not (loc[0]+1,loc[1]) in maze[loc][0] and len(maze[loc][1]) > 0:
                self.x -= self.dx
            if self.x > xfen - 15 - img_kresh.get_width() and not (loc[0]+1,loc[1]) in maze[loc][0]:
                self.x -= self.dx
            elif self.x > xfen - img_kresh.get_width() and (loc[0]+1,loc[1]) in maze[loc][0]:
                loc = (loc[0]+1,loc[1])
                self.x = 20
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

            if self.y > yfen - 15 - img_kresh.get_height() and not (loc[0],loc[1]+1) in maze[loc][0]and len(maze[loc][1]) > 0:
                self.y -= self.dy
            elif self.y > yfen - 15 - img_kresh.get_height() and not (loc[0],loc[1]+1) in maze[loc][0]:
                self.y -= self.dy
            elif self.y > yfen - img_kresh.get_height() and (loc[0],loc[1]+1) in maze[loc][0]:
                loc = (loc[0],loc[1]+1)
                self.y = 20
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

            if self.y < 15  and not (loc[0],loc[1]-1) in maze[loc][0] and len(maze[loc][1]) > 0:
                self.y -= self.dy
            elif self.y < 15  and not (loc[0],loc[1]-1) in maze[loc][0]:
                self.y -= self.dy
            elif self.y < 0 and (loc[0],loc[1]-1) in maze[loc][0]:
                loc = (loc[0],loc[1]-1)
                self.y = yfen - 20 - img_kresh.get_height()
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

            if self.x < 15  and (loc[0]-1,loc[1]) in maze[loc][0] and len(maze[loc][1]) > 0:
                self.x -= self.dx
            elif self.x < 15  and not (loc[0]-1,loc[1]) in maze[loc][0] :
                self.x -= self.dx
            elif self.x < 0 and (loc[0]-1,loc[1]) in maze[loc][0]:
                loc = (loc[0]-1,loc[1])

                self.x = xfen - 20 - img_kresh.get_width()
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

        fen.blit(img_kresh, (self.x,self.y))


class Ennemy:
    def __init__(self, joueur):
        self.x = random.randint(80, xfen - 100)
        self.y = random.randint(80, xfen - 100)
        self.speed = random.randint(1, 3)
        self.clock = 0  # frame checker
        self.moveclock = random.randint(20, 30)  # moves on the x frame then reset
        self.ennemie_races = ['alien']
        self.race = random.choice(self.ennemie_races)
        self.joueur = joueur

    def move(self):
        if self.clock >= self.moveclock:
            self.clock = 0

            angle = math.atan2(self.joueur.y - self.y, self.joueur.x - self.x)
            print(angle)
            self.x += math.cos(angle) * self.speed
            self.y += math.sin(angle) * self.speed
        else:
            self.clock += 1
        fen.blit(img_ennemie,(self.x,self.y))


def spawner(maze):
    spawn_x = random.randint(0,dimx-1)
    spawn_y = random.randint(0,dimy-1)
    if len(maze[(spawn_x,spawn_y)][0]) > 0:
        return (spawn_x,spawn_y)
    else:
        spawner(maze)



def afficher_mur(maze,loc):

    fen.fill((100,100,100))

    pygame.draw.circle(fen,(200,80,50),(0,0),15)
    pygame.draw.circle(fen,(200,80,50),(xfen,0),15)
    pygame.draw.circle(fen,(200,80,50),(0,yfen),15)
    pygame.draw.circle(fen,(200,80,50),(xfen,yfen),15)


    if len(maze[loc][1]) > 0:
        pygame.draw.line(fen,(200,150,150),(xfen,0),(xfen,yfen),30)
        pygame.draw.line(fen,(200,150,150),(0,0),(0,yfen),30)
        pygame.draw.line(fen,(200,150,150),(0,0),(xfen,0),30)
        pygame.draw.line(fen,(200,150,150),(0,yfen),(xfen,yfen),30)

    if not (loc[0]+1,loc[1]) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(xfen,0),(xfen,yfen),30)

    if not (loc[0]-1,loc[1]) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(0,0),(0,yfen),30)

    if not (loc[0],loc[1]-1) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(0,0),(xfen,0),30)

    if not (loc[0],loc[1]+1) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(0,yfen),(xfen,yfen),30)



def spawn_ennemies(visited,maze,loc):
    if not loc in visited:
        for _ in range(random.randint(3,7)):
            maze[loc][1].append(Ennemy(kresh))

kresh = Joueur()

spawn = spawner(maze)
print(spawn)

visited = [spawn]


loc = spawn





clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)

    afficher_mur(maze,loc)


    kresh.move()
    if len(maze[loc][1]) > 0:
        for ennemi in maze[loc][1]:
            ennemi.move()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()