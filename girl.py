import pygame
import sys

pygame.init()
size = (800,600)
image = "res/walking_animation.png"
screen = pygame.display.set_mode(size)
x = 400
y = 200
speed_x = 3
speed_y = 3
clock = pygame.time.Clock()


while True:
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.QUIT:
        pygame.exit()
        sys.exit()
  screen.fill(255, 255, 255)
    
  pygame.draw.rect(screen, image, (x,y,80,80))
  pygame.display.flip()
  if (x > 800 or x < 0):
    speed_x*=-1  
    x+=speed_x

clock.tick(60)
