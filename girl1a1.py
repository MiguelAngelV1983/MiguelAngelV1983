import pygame
import os


class Girl:
    
    
    pygame.init()

    coord_x=800
    coord_y=480

    speed_x = 3
    
    screen = pygame.display.set_mode([coord_x, coord_y], 0, 32)
    

    myGirl = pygame.image.load("./res/walking_animation.png")
    miniGirlR = dict()
    miniGirlL = dict()
    miniGirlR[0] = myGirl.subsurface((0,0),(63,127)) #(X inicio, Y inicio)(X tamaño, Y tamaño)
    miniGirlR[1] = myGirl.subsurface((64,0), (63,127))
    miniGirlR[2] = myGirl.subsurface((128,0), (63,127))
    miniGirlR[3] = myGirl.subsurface((192,0), (63,127))
    miniGirlR[4] = myGirl.subsurface((256,0), (63,127))
    miniGirlR[5] = myGirl.subsurface((320,0), (63,127))
    miniGirlR[6] = myGirl.subsurface((384,0), (63,127))
    miniGirlR[7] = myGirl.subsurface((448,0), (63,127))
    miniGirlR[8] = myGirl.subsurface((512,0), (63,127))
    miniGirlR[9] = myGirl.subsurface((576,0), (63,127))
    miniGirlL[0] = myGirl.subsurface((0,128),(63,127)) #(X inicio, Y inicio)(X tamaño, Y tamaño)
    miniGirlL[1] = myGirl.subsurface((64,128), (63,127))
    miniGirlL[2] = myGirl.subsurface((128,128), (63,127))
    miniGirlL[3] = myGirl.subsurface((192,128), (63,127))
    miniGirlL[4] = myGirl.subsurface((256,128), (63,127))
    miniGirlL[5] = myGirl.subsurface((320,128), (63,127))
    miniGirlL[6] = myGirl.subsurface((384,128), (63,127))
    miniGirlL[7] = myGirl.subsurface((448,128), (63,127))
    miniGirlL[8] = myGirl.subsurface((512,128), (63,127))
    miniGirlL[9] = myGirl.subsurface((576,128), (63,127))


    x, y = screen.get_width()/15, 100
    move_x, move_y = 0, 0
    sprite_num = 0
    sprite_lr = True

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

            elif event.type == pygame.K_RIGHT:
                if event.key == pygame.K_LEFT:
                    move_x = -0.1
                    screen.blit(miniGirlL[1], (x, y))
                elif event.key == pygame.K_RIGHT:
                    move_x = +0.1
                    screen.blit(miniGirlR[1], (x, y))

        x+= move_x
        y+= move_y


##        if (move_x > coord_x or move_x < 0):
##            if move_x > coord_x:
##                move_x = coord_x
##            elif move_x < 0:
##                move_x = 0

        screen.fill((0, 225, 255))

        
        
        screen.blit(miniGirlR[0], (x, y))
        screen.blit(miniGirlL[0], (x, y+128))
        
        

        



        pygame.display.update()

    pygame.quit()
