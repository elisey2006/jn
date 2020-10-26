import pygame
W, H = 800, 600
BLUE = (192, 192, 192)
BLACK = (50, 50, 50)
numeral = ''
start = 1

pygame.init()
pygame.display.set_caption('тест')
screen = pygame.display.set_mode((W, H))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            
screen.fill