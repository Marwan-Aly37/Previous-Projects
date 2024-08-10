import pygame as pg
pg.init()
screen = pg.display.set_mode([600,600])
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255, 255, 255))
   # pg.draw.rect(screen, (0, 0, 0), (0, 0, 85.3125, 85.3125), 0)
    #pg.draw.rect(screen, (0, 0, 0), (170.625, 0, 85.3125, 85.3125), 0)
    #pg.draw.rect(screen, (0, 0, 0), (341.25, 0, 85.3125, 85.3125), 0)
    #pg.draw.rect(screen, (0, 0, 0), (511.875, 0, 85.3125, 85.3125), 0)
    #pg.draw.rect(screen, (0, 0, 0), (682.5, 0, 85.3125, 85.3125), 0)
    #pg.draw.rect(screen, (0, 0, 0), (853.125, 0, 85.3125, 85.3125), 0)
    #pg.draw.rect(screen, (0, 0, 0), (1023.75, 0, 85.3125, 85.3125), 0)
    #pg.draw.rect(screen, (0, 0, 0), (1194.375, 0, 85.3125, 85.3125), 0)
    for square in range(8):
        pg.draw.rect(screen, (0, 0, 0), (150*square, 0, 75, 75), 0)
        
        for squ in range(8):
            pg.draw.rect(screen, (0, 0, 0), (150*square, 150*(squ+1), 75, 75), 0)
    for square in range(16):
        if square%2!=0:
            pg.draw.rect(screen,(0,0,0),(75*square,75,75,75),0)
            for squ in range(16):
                if squ%2!=0:
                    pg.draw.rect(screen,(0,0,0),(75*square,75*squ,75,75),0)
    pawn = pygame.image.load('C:\Users\marwa\OneDrive\Pictures\pawn_black.png')



    pg.display.flip()

pg.quit()