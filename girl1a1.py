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
                    move_x = -1
                    sprite_lr = False
                    if(sprite_num == 0):
                        sprite_num = 9
                    else:
                        sprite_num -= 1
                elif event.key == pygame.K_RIGHT:
                    move_x = +1
                    sprite_lr = True
                    if(sprite_num == 9):
                        sprite_num = 0
                    else:
                        sprite_num += 1
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_x = 0
                elif event.key == pygame.K_RIGHT:
                    move_x = 0

            elif event.type == pygame.K_RIGHT:
                if event.key == pygame.K_LEFT:
                    move_x = -1
                elif event.key == pygame.K_RIGHT:
                    move_x = +1
                    sprite_num += 1
                    
        x+= move_x
        y+= move_y

        if(x < 0):
            x = 0

        if(x > coord_x-64):
            x = coord_x-64

        

        print(x)


        screen.fill((0, 225, 255))
        if(sprite_lr == True):
            screen.blit(miniGirlR[sprite_num], (x, y))
        else:
            screen.blit(miniGirlL[sprite_num], (x, y))
        
##        for i in range(0,9):
##            
##            
##            x+=0.05
##            if (x==coord_x):
##                for j in range(9,0):
##                    x+=0.05
##                    screen.blit(miniGirlL[j], (x, y+128))
        
        

        



        pygame.display.update()

    pygame.quit()
