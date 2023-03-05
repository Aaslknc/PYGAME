import pygame
from moveObj import moveObj

pygame.init()
SCREEN_WIDHT, SCREEN_HEIGHT = 600,400
GREEN = (0,255,0)
WHITE = (255,255,255)
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('Import_Study')
running = True
clock = pygame.time.Clock()

# shapes (assume we can have multiple shapes in a pygame program)

s1 = {'objRect': pygame.Rect(20,20,30,30), 'color': GREEN, 'vel': [-5,5], 'shape': 'square'}

shapes = [s1]

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for shape in shapes:
        moveObj(shape, (SCREEN_WIDHT, SCREEN_HEIGHT))

        if shape['shape'] == 'square':
            pygame.draw.rect(screen, shape['color'], shape['objRect'])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
