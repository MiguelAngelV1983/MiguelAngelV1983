import pygame
import os


class Girl:
    
    
    pygame.init()

    coord_x=800
    coord_y=480

    speed_x = 3
    
    screen = pygame.display.set_mode([coord_x, coord_y], 0, 32)
    

    myGirl = pygame.image.load("./res/walking_animation.png")
    miniGirl = dict()
    miniGirl[0] = myGirl.subsurface((0,0), (50,130))
    miniGirl[1] = myGirl.subsurface((130,50), (50,130))
    miniGirl[2] = myGirl.subsurface((260,50), (50,130))
    miniGirl[3] = myGirl.subsurface((390,50), (50,130))
    miniGirl[4] = myGirl.subsurface((520,50), (50,130))
    miniGirl[5] = myGirl.subsurface((50,0), (10,5))
    miniGirl[6] = myGirl.subsurface((60,0), (10,5))
    miniGirl[7] = myGirl.subsurface((70,0), (10,5))
    miniGirl[8] = myGirl.subsurface((80,0), (10,5))
    miniGirl[9] = myGirl.subsurface((90,0), (10,5))


    x, y = screen.get_width()/15, 100
    move_x, move_y = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_x = -0.1
                elif event.key == pygame.K_RIGHT:
                    move_x = +0.1
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_x = 0
                elif event.key == pygame.K_RIGHT:
                    move_x = 0

        x+= move_x
        y+= move_y


##        if (move_x > coord_x or move_x < 0):
##            if move_x > coord_x:
##                move_x = coord_x
##            elif move_x < 0:
##                move_x = 0

        screen.fill((0, 225, 255))

        
        for i in range (0,10):
            screen.blit(miniGirl[i], (x, y))



        pygame.display.update()

    pygame.quit()
