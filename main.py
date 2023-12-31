import pygame,math,random,map_maker,maze_vizualiser
from image_loader import*

xfen,yfen = 1600,900
dimx,dimy = 6,6
multix,multiy = xfen/dimx , yfen/dimy

maze = maze_vizualiser.show(dimx,dimy)
pygame.init()
fen = pygame.display.set_mode((xfen,yfen),pygame.FULLSCREEN)#


class Spell:
    def __init__(self,name,x,y):
        global kresh
        self.joueur = kresh
        self.name = name
        self.x = x
        self.y = y
        self.rect = pygame.Rect(-2,-2,1,1)
        if self.name == 'lazer_r':
            self.speed = 30
            self.rect = pygame.Rect(self.x,self.y,20,5)
        elif self.name == 'lazer_d':
            self.speed = 30
            self.rect = pygame.Rect(self.x,self.y,5,20)
        elif self.name == 'lazer_u':
            self.speed = -30
            self.rect = pygame.Rect(self.x,self.y,5,-20)
        elif self.name == 'lazer_l':
            self.speed = -30
            self.rect = pygame.Rect(self.x,self.y,-20,5)

        elif self.name == 'molo_r':
            self.speed = 25
            self.speed_y = -30
            self.temp_vie = 60 * 3
        elif self.name == 'molo_l':
            self.speed = 25
            self.speed_y = -30
            self.temp_vie = 60 * 3
        elif self.name == 'molo_u':
            self.speed_y = -25
            self.temp_vie = 60 * 3
        elif self.name == 'molo_d':
            self.speed_y = 25
            self.temp_vie = 60 * 3


    def step(self):
        if self.name == 'lazer_r':
            self.lazer('droite')

        elif self.name == 'lazer_d':
            self.lazer('bas')

        elif self.name == 'lazer_u':
            self.lazer('haut')

        elif self.name == 'lazer_l':
            self.lazer('gauche')

        elif self.name == 'molo_r':
            self.molo('droite')
        elif self.name == 'molo_l':
            self.molo('gauche')
        elif self.name == 'molo_d':
            self.molo('bas')
        elif self.name == 'molo_u':
            self.molo('haut')

    def molo(self,dirrection):
        if dirrection == 'droite':
            if self.speed_y < 25:
                self.x += self.speed
                self.y += self.speed_y
                self.speed_y += 3

                fen.blit(molo,(self.x,self.y))
            else:
                self.temp_vie -= 1
                if self.temp_vie > 0:
                    fen.blit(fire,(self.x,self.y))
                    self.rect = pygame.Rect(self.x,self.y,fire.get_width(),fire.get_height())
                else:
                    self.joueur.spells.remove(self)
        if dirrection == 'gauche':
            if self.speed_y < 25:
                self.x -= self.speed
                self.y += self.speed_y
                self.speed_y += 2.7

                fen.blit(molo,(self.x,self.y))
            else:
                self.temp_vie -= 1
                if self.temp_vie > 0:
                    fen.blit(fire,(self.x,self.y))
                    self.rect = pygame.Rect(self.x,self.y,fire.get_width(),fire.get_height())
                else:
                    self.joueur.spells.remove(self)
        if dirrection == 'haut':
            if self.speed_y < 0:
                self.y += self.speed_y
                self.speed_y += 0.7

                fen.blit(molo,(self.x,self.y))
            else:
                self.temp_vie -= 1
                if self.temp_vie > 0:
                    fen.blit(fire,(self.x,self.y))
                    self.rect = pygame.Rect(self.x,self.y,fire.get_width(),fire.get_height())
                else:
                    self.joueur.spells.remove(self)
        if dirrection == 'bas':
            if self.speed_y > 0:
                self.y += self.speed_y
                self.speed_y -= 0.7

                fen.blit(molo,(self.x,self.y))
            else:
                self.temp_vie -= 1
                if self.temp_vie > 0:
                    fen.blit(fire,(self.x,self.y))
                    self.rect = pygame.Rect(self.x,self.y,fire.get_width(),fire.get_height())
                else:
                    self.joueur.spells.remove(self)

    def lazer(self,dirrection):
        if dirrection == 'droite':
            self.x += self.speed
            self.rect = pygame.Rect(self.x,self.y,20,5)
            pygame.draw.rect(fen,(255,0,0),self.rect)
        elif dirrection == 'gauche':
            self.x += self.speed
            self.rect = pygame.Rect(self.x,self.y,-20,5)
            pygame.draw.rect(fen,(255,0,0),self.rect)
        elif dirrection == 'haut':
            self.y += self.speed
            self.rect = pygame.Rect(self.x,self.y,5,-20)
            pygame.draw.rect(fen,(255,0,0),self.rect)
        elif dirrection == 'bas':
            self.y += self.speed
            self.rect = pygame.Rect(self.x,self.y,5,20)
            pygame.draw.rect(fen,(255,0,0),self.rect)


class Joueur:
    def __init__(self):
        self.speed = 8
        self.x = xfen/2 - img_kresh.get_width()/2
        self.y = yfen/2 - img_kresh.get_height()/2
        self.dx,self.dy = 0,0
        self.image = img_kresh_aie
        self.rect = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        self.vie = 6
        self.imunite = 60
        self.counter_imunite = 60
        self.combo = []
        self.patience = 10
        self.spells = []
        self.joueur = self
        self.spell_table = {
                            ():None,
                            ('droite',):'lazer_r',
                            ('gauche',):'lazer_l',
                            ('bas',):'lazer_d',
                            ('haut',):'lazer_u',
                            ('droite','droite','droite'):'molo_r',
                            ('gauche','gauche','gauche'):'molo_l',
                            ('haut','haut','haut'):'molo_u',
                            ('bas','bas','bas'):'molo_d'
                           }

    def attack(self):

        for u,i in enumerate(self.combo):
            if i == 'droite':
                fen.blit(arrow_r,(self.x-50 + 55*u,self.y-45))
            if i == 'gauche':
                fen.blit(arrow_l,(self.x-50 + 55*u,self.y-45))
            if i == 'haut':
                fen.blit(arrow_u,(self.x-50 + 55*u,self.y-45))
            if i == 'bas':
                fen.blit(arrow_d,(self.x-50 + 55*u,self.y-45))


        for spell in self.spells:
            spell.step()

    def add_combo(self,keys):
        if self.patience >= 15:
            if len(self.combo) < 3:
                if keys[pygame.K_UP]:
                    self.combo.append('haut')
                elif keys[pygame.K_DOWN]:
                    self.combo.append('bas')
                elif keys[pygame.K_LEFT]:
                    self.combo.append('gauche')
                elif keys[pygame.K_RIGHT]:
                    self.combo.append('droite')
                self.patience = 0
        else:
            self.patience += 1

        if keys[pygame.K_SPACE]:
            self.patience = 0
            if tuple(self.combo) in self.spell_table:

                self.spells.append(Spell(self.spell_table[tuple(self.combo)],self.x+self.image.get_width()/2,self.y+self.image.get_height()/2))
            else:
                self.combo = []
                fen.blit(error,(self.x-50 + 50,self.y-50))

            self.combo = []


    def move(self):
        global loc
        keys = pygame.key.get_pressed()
        self.add_combo(keys)

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

            if self.x > xfen - 15 - img_kresh.get_width() and (loc[0]+1,loc[1]) in maze[loc][0] and len(maze[loc][1]) > 0:
                self.x -= self.dx
            if self.x > xfen - 15 - img_kresh.get_width() and not (loc[0]+1,loc[1]) in maze[loc][0]:
                self.x -= self.dx
            elif self.x > xfen - img_kresh.get_width() and (loc[0]+1,loc[1]) in maze[loc][0]:
                loc = (loc[0]+1,loc[1])
                self.spells = []
                self.x = 20
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

            if self.y > yfen - 15 - img_kresh.get_height() and  (loc[0],loc[1]+1) in maze[loc][0]and len(maze[loc][1]) > 0:
                self.y -= self.dy
            elif self.y > yfen - 15 - img_kresh.get_height() and not (loc[0],loc[1]+1) in maze[loc][0]:
                self.y -= self.dy
            elif self.y > yfen - img_kresh.get_height() and (loc[0],loc[1]+1) in maze[loc][0]:
                loc = (loc[0],loc[1]+1)
                self.spells = []
                self.y = 20
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

            if self.y < 15  and (loc[0],loc[1]-1) in maze[loc][0] and len(maze[loc][1]) > 0:
                self.y -= self.dy
            elif self.y < 15  and not (loc[0],loc[1]-1) in maze[loc][0]:
                self.y -= self.dy
            elif self.y < 0 and (loc[0],loc[1]-1) in maze[loc][0]:
                loc = (loc[0],loc[1]-1)
                self.spells = []
                self.y = yfen - 20 - img_kresh.get_height()
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

            if self.x < 15  and (loc[0]-1,loc[1]) in maze[loc][0] and len(maze[loc][1]) > 0:
                self.x -= self.dx
            elif self.x < 15  and not (loc[0]-1,loc[1]) in maze[loc][0] :
                self.x -= self.dx
            elif self.x < 0 and (loc[0]-1,loc[1]) in maze[loc][0]:
                loc = (loc[0]-1,loc[1])
                self.spells = []
                self.x = xfen - 20 - img_kresh.get_width()
                spawn_ennemies(visited,maze,loc)
                visited.append(loc)

        self.rect = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        fen.blit(self.image, (self.x,self.y))

    def colision(self,ennemies):
        global run,run1
        for ennemie in ennemies:
            if ennemie.rect.colliderect(self.rect):
                if self.counter_imunite >= self.imunite:
                    self.vie -= 1
                    self.counter_imunite = 0

            if ennemie.race == 'shooter':
                for bullet in ennemie.bullets:
                    if bullet.rect.colliderect(self.rect):
                        ennemie.bullets.remove(bullet)
                        if self.counter_imunite >= self.imunite:
                            self.vie -= 1
                            self.counter_imunite = 0

        if self.counter_imunite < self.imunite:
            self.image = img_kresh_aie
        else:
            self.image = img_kresh

        self.counter_imunite += 1

        if self.vie < 1:
            run = False
            run1 = True



class Ennemy:
    def __init__(self, joueur):
        self.tirage = []
        for i in range(70):
            self.tirage.append('débile')
        for i in range(30):
            self.tirage.append('shooter')

        self.race = random.choice(self.tirage)
        self.joueur = joueur
        self.attribution_stats()
        self.face=True

    def get_hit(self):
        for spell in self.joueur.spells:
            if spell.rect.colliderect(self.rect):
                if spell.name[:-2] == 'molo':
                    pass
                else:
                    self.joueur.spells.remove(spell)
                self.vie -= 1
        if self.vie < 1:
            maze[loc][1].remove(self)

    def attribution_stats(self):
        if self.race == 'débile':
            self.vie = 2
            self.image = img_ennemie
            self.image.set_colorkey((255,255,255))
            self.x = random.randint(160, xfen - 160)
            self.y = random.randint(160, yfen - 160)
            self.speed = random.randint(10, 14)
            self.clock = 0  # frame checker
            self.moveclock = random.randint(8, 15)
            self.image_fliped = pygame.transform.flip(self.image,True,False)
            self.image_fliped.set_colorkey((255,255,255))
            self.rect = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())

        elif self.race == 'shooter':
            self.vie = 1
            self.bullets = []
            self.shot_speed = random.randint(3,6)
            self.attack_timer = random.randint(80,120)
            self.attack_clock = random.randint(0,80)
            self.image = img_ennemie_shooter
            self.image.set_colorkey((255,255,255))
            self.x = random.randint(500, xfen - 500)
            self.y = random.randint(400, yfen - 400)
            self.speed = random.randint(1, 6)
            self.clock = 0  # frame checker
            self.moveclock = random.randint(10, 19)
            self.image_fliped = pygame.transform.flip(self.image,True,False)
            self.image_fliped.set_colorkey((255,255,255))
            self.rect = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())


    def move(self):
        if self.clock >= self.moveclock:
            self.clock = 0
            hypothenuse = math.sqrt((self.joueur.y - self.y)**2 + (self.joueur.x - self.x)**2)

            if hypothenuse > 60 and self.race == 'débile':
                angle = math.atan2(self.joueur.y - self.y, self.joueur.x - self.x)
                self.x += math.cos(angle) * self.speed
                self.y += math.sin(angle) * self.speed
            elif hypothenuse > 250 and self.race == 'shooter':
                angle = math.atan2(self.joueur.y - self.y, self.joueur.x - self.x)
                self.x += math.cos(angle) * self.speed
                self.y += math.sin(angle) * self.speed
            self.rect = pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        else:
            self.clock += 1

        if self.joueur.x - self.x > 0:
            fen.blit(self.image,(self.x,self.y))
        else:
            fen.blit(self.image_fliped,(self.x,self.y))

    def attack(self):

        if self.race == 'shooter':
            for bullet in self.bullets:
                bullet.step()
                if not 0 < bullet.x < xfen + 10 or not 0 < bullet.y < yfen + 10:
                    self.bullets.remove(bullet)

            if self.attack_clock > self.attack_timer:
                self.attack_clock = 0

                dx = math.cos(math.atan2(self.joueur.y - self.y, self.joueur.x - self.x)) * self.shot_speed
                dy = math.sin(math.atan2(self.joueur.y - self.y, self.joueur.x - self.x)) * self.shot_speed
                self.bullets.append(Ennemy_shot(self.x+self.image.get_width()/2,self.y+self.image.get_height()/2,dx,dy))

            else:
                self.attack_clock += 1

class Ennemy_shot:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rect = pygame.Rect(self.x-5,self.y-5,5,5)

    def step(self):
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x-5,self.y-5,5,5)
        pygame.draw.circle(fen,(230,40,60),(self.x,self.y),5)


def spawner(maze):
    spawn_x = random.randint(0,dimx-1)
    spawn_y = random.randint(0,dimy-1)
    if len(maze[(spawn_x,spawn_y)][0]) > 0:
        return (spawn_x,spawn_y)
    else:
        spawner(maze)



def afficher_mur(maze,loc):

    fen.fill((100,100,100))

    if len(maze[loc][1]) > 0:
        pygame.draw.line(fen,(100,50,50),(xfen,0),(xfen,yfen),30)
        pygame.draw.line(fen,(100,50,50),(0,0),(0,yfen),30)
        pygame.draw.line(fen,(100,50,50),(0,0),(xfen,0),30)
        pygame.draw.line(fen,(100,50,50),(0,yfen),(xfen,yfen),30)

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



def afficher_hearth(vie):
    global hearth,hearth_holder
    hearth_holder = pygame.transform.scale(pygame.image.load('images/hearth_holder.png'),(pygame.image.load('images/hearth_holder.png').get_width()*2,pygame.image.load('images/hearth_holder.png').get_height()*2))
    hearth_holder.set_colorkey((255,255,255))
    if vie > 5:
        hearth_holder = pygame.transform.scale(hearth_holder,(hearth_holder.get_width() + (vie-5) * hearth.get_width() + 2*(vie-5),hearth_holder.get_height()))
        hearth_holder.set_colorkey((255,255,255))


    fen.blit(hearth_holder,(0,0))
    for i in range(vie):
        fen.blit(hearth,(4 + i*hearth.get_width() + i*3,6))



def spawn_ennemies(visited,maze,loc):
    if not loc in visited:
        for _ in range(random.randint(15,20)):
            maze[loc][1].append(Ennemy(kresh))

kresh = Joueur()

spawn = spawner(maze)
print(spawn)

visited = [spawn]
loc = spawn

clock = pygame.time.Clock()
run1 = False
run = True
while run:
    clock.tick(60)

    afficher_mur(maze,loc)
    afficher_hearth(kresh.vie)


    kresh.move()
    kresh.colision(maze[loc][1])
    kresh.attack()
    if len(maze[loc][1]) > 0:
        for ennemi in maze[loc][1]:
            ennemi.move()
            ennemi.attack()
            ennemi.get_hit()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

if run1:
    fen.blit(img_lost,(0,0))
while run1:
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run1 = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run1 = False
                pygame.quit()
pygame.quit()