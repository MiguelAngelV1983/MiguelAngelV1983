import pygame
import os


class Girl:
    
    def __init():
        
            pygame.init()

            
            

            

    def __update():
        
            coord_x=1000
            coord_y=250

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


            x, y = screen.get_width()/15, coord_y-127
            move_x, move_y = 0, 0
            sprite_num = 0
            sprite_lr = True

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            

                
                if (sprite_lr == True) and (x <= coord_x-64):
                    x += 1
                    if(sprite_num > 9):
                        sprite_num = 1
                    else:
                        sprite_num += 0.05
                elif (sprite_lr == False) and (x >= 0):
                    x -= 1
                    if(sprite_num > 9):
                        sprite_num = 1
                    else:
                        sprite_num += 0.05
                      
                            

                if(x < 0):
                    x = 0
                    sprite_lr = True


                if(x > coord_x-64):
                    x = coord_x-64
                    sprite_lr = False

                

                print(x)
                print(sprite_num)


                screen.fill((0, 225, 255))
                if(sprite_lr == True):
                    screen.blit(miniGirlR[round(sprite_num)], (x, y))
                else:
                    screen.blit(miniGirlL[round(sprite_num)], (x, y))
                


                pygame.display.update()
                

    __init()
    __update()
    pygame.quit()
