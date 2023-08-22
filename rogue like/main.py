import pygame,math,random,map_maker,maze_vizualiser

img_kresh = pygame.transform.scale(pygame.image.load('shrek.png'),(50,80))
img_kresh.set_colorkey((255,255,255))

xfen,yfen = 800,800
dimx,dimy = 6,6
multix,multiy = xfen/dimx , yfen/dimy

maze = maze_vizualiser.show(dimx,dimy)

pygame.init()

fen = pygame.display.set_mode((xfen,yfen))

class Joueur:
    def __init__(self):
        self.speed = 5
        self.x = xfen/2 - img_kresh.get_width()/2
        self.y = yfen/2 - img_kresh.get_height()/2

    def move(self):
        keys = pygame.key.get_pressed()

        if not (keys[pygame.K_z] and keys[pygame.K_d] and keys[pygame.K_s] and keys[pygame.K_q]):

            if keys[pygame.K_z] and keys[pygame.K_d]:
                self.x += self.speed *  math.sqrt(2) / 2
                self.y -= self.speed * math.sqrt(2) / 2

            elif keys[pygame.K_z] and keys[pygame.K_q]:
                self.x -= self.speed * math.sqrt(2) / 2
                self.y -= self.speed * math.sqrt(2) / 2

            elif keys[pygame.K_s] and keys[pygame.K_d]:
                self.x += self.speed * math.sqrt(2) / 2
                self.y += self.speed * math.sqrt(2) / 2

            elif keys[pygame.K_s] and keys[pygame.K_q]:
                self.x -= self.speed * math.sqrt(2) / 2
                self.y += self.speed * math.sqrt(2) / 2

            if keys[pygame.K_z] and not keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_q]:
                self.y -= self.speed

            elif not keys[pygame.K_z] and keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_q]:
                self.x += self.speed

            elif not keys[pygame.K_z] and not keys[pygame.K_d] and keys[pygame.K_s] and not keys[pygame.K_q]:
                self.y += self.speed

            elif not keys[pygame.K_z] and not keys[pygame.K_d] and not keys[pygame.K_s] and keys[pygame.K_q]:
                self.x -= self.speed
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



spawn = None

def spawner(maze):
    global spawn

    spawn_x = random.randint(0,dimx-1)
    spawn_y = random.randint(0,dimy-1)
    if len(maze[(spawn_x,spawn_y)][0]) > 0:
        spawn = (spawn_x,spawn_y)
    else:
        spawner(maze)



def afficher_mur(maze,loc):

    fen.fill((100,100,100))

    pygame.draw.circle(fen,(200,80,50),(0,0),15)
    pygame.draw.circle(fen,(200,80,50),(xfen,0),15)
    pygame.draw.circle(fen,(200,80,50),(0,yfen),15)
    pygame.draw.circle(fen,(200,80,50),(xfen,yfen),15)


    if not (loc[0]+1,loc[1]) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(xfen,0),(xfen,yfen),30)

    if not (loc[0]-1,loc[1]) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(0,0),(0,yfen),30)

    if not (loc[0],loc[1]-1) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(0,0),(xfen,0),30)

    if not (loc[0],loc[1]+1) in maze[loc][0]:
        pygame.draw.line(fen,(200,80,50),(0,yfen),(xfen,yfen),30)


kresh = Joueur()

spawner(maze)

loc = spawn
print(spawn)





clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)

    afficher_mur(maze,loc)


    kresh.move()


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()