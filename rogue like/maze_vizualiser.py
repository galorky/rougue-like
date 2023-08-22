import pygame,map_maker
pygame.init()

def show(dimx,dimy):
    xfen,yfen = 1920,1080
    multix,multiy = xfen/dimx,yfen/dimy


    fen = pygame.display.set_mode((xfen,yfen),pygame.FULLSCREEN)

    maze = map_maker.generate(dimx,dimy)

    for i in maze:
        for o in maze[i][0]:
            pygame.draw.line(fen,(255,255,255),(i[0]*multix,i[1]*multiy),(o[0]*multix,o[1]*multiy),5)

    for i in maze:
        pygame.draw.circle(fen,(255,0,0),(i[0]*multix,i[1]*multiy),5)

    pygame.display.update()

    pygame.image.save(fen, "screenshot.png")
    pygame.quit()
    return maze



