import pygame
xfen,yfen = 1600,900

img_lost = pygame.transform.scale(pygame.image.load('lost.png'),(xfen,yfen))

img_kresh = pygame.transform.scale(pygame.image.load('shrek.png'),(50,80))
img_kresh.set_colorkey((255,255,255))

img_kresh_aie = pygame.transform.scale(pygame.image.load('shrek_aie.png'),(50,80))
img_kresh_aie.set_colorkey((255,255,255))

img_ennemie = pygame.transform.scale(pygame.image.load('ennemie.png'),(50,80))
img_ennemie.set_colorkey((255,255,255))

img_ennemie_shooter = pygame.transform.scale(pygame.image.load('ennemie_shooter.png'),(70,80))
img_ennemie_shooter.set_colorkey((255,255,255))

hearth = pygame.transform.scale(pygame.image.load('hearth.png'),(pygame.image.load('hearth.png').get_width()*2,pygame.image.load('hearth.png').get_height()*2))
hearth.set_colorkey((255,255,255))

hearth_holder = pygame.transform.scale(pygame.image.load('hearth_holder.png'),(pygame.image.load('hearth_holder.png').get_width()*2,pygame.image.load('hearth_holder.png').get_height()*2))
hearth_holder.set_colorkey((255,255,255))


arrow_r = pygame.transform.scale(pygame.image.load('arrow_r.png'),(pygame.image.load('arrow_r.png').get_width()*2,pygame.image.load('arrow_r.png').get_height()*2))
arrow_r.set_colorkey((255,255,255))

arrow_d = pygame.transform.scale(pygame.image.load('arrow_d.png'),(pygame.image.load('arrow_d.png').get_width()*2,pygame.image.load('arrow_d.png').get_height()*2))
arrow_d.set_colorkey((255,255,255))

arrow_u = pygame.transform.scale(pygame.image.load('arrow_u.png'),(pygame.image.load('arrow_u.png').get_width()*2,pygame.image.load('arrow_u.png').get_height()*2))
arrow_u.set_colorkey((255,255,255))

arrow_l = pygame.transform.scale(pygame.image.load('arrow_l.png'),(pygame.image.load('arrow_l.png').get_width()*2,pygame.image.load('arrow_l.png').get_height()*2))
arrow_l.set_colorkey((255,255,255))