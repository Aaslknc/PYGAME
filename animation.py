import pygame
import time
import random

pygame.init()

# varibles
running = True
SCREEN_HEIGHT = 400
SCREEN_WIDHT = 600
screen = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))
pygame.display.set_caption('Test')

# colors
WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (200,0,0)
BLUE = (0,0,200)
BLACK = (0,0,0)
YELLOW = (255,200,0)
GRAY = (128,128,128)

colors = [WHITE, GREEN, RED, BLUE, YELLOW]

# font and text
font = pygame.font.Font(None, 48)
text = font.render('Animation Study', True, YELLOW, None)

# main animation function
def moveObj(shape, screen_dim):
    screen_bottom = 0
    screen_right = screen_dim[0]
    screen_left = 0
    screen_top = screen_dim[1]
    touched_borders = False

    # test for first rectangle
    if shape['shape'] == 'rectangle':
        # check if object has passed the screen borders
        if shape['objRect'].top + 60 > screen_top or shape['objRect'].bottom - 60< screen_bottom:
            shape['vel'][1] = shape['vel'][1] * (-1)
            touched_borders = True

        if shape['objRect'].left < screen_left or shape['objRect'].right > screen_right:
            shape['vel'][0] = shape['vel'][0] * (-1)
            touched_borders = True
    
    # test for second rectangle (rectangle1)
    if shape['shape'] == 'rectangle1':
        if shape['objRect'].top + 100 > screen_top or shape['objRect'].bottom - 100< screen_bottom:
            shape['vel'][1] = shape['vel'][1] * (-1)
            touched_borders = True

        if shape['objRect'].left < screen_left or shape['objRect'].right > screen_right:
            shape['vel'][0] = shape['vel'][0] * (-1)
            touched_borders = True
        
    
    # this is where the real sugar happens
    shape['objRect'].x += shape['vel'][0]
    shape['objRect'].y += shape['vel'][1]
    
    # if the rect has touched the borders
    if touched_borders:
        shape['color'] = random.choice(colors)
       




# shapes
s1 = {'objRect': pygame.Rect(100,200,60,60), 'color': GREEN, 'vel': [-5,5], 'shape': 'rectangle'}
s2 = {'objRect': pygame.Rect(100,200,100,100), 'color': YELLOW, 'vel': [1,5], 'shape': 'rectangle1'}

rect_pos_x = 500
shapes = [s1,s2]


# main game loop
while running:
    screen.fill(GRAY)
    screen.blit(text, [100,100])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # calls the moveObj function for every shape in shapes
    for shape in shapes:
        moveObj(shape, (SCREEN_WIDHT, SCREEN_HEIGHT))

        if shape['shape'] == 'rectangle':
            pygame.draw.rect(screen, shape['color'], shape['objRect'])
        if shape['shape'] == 'rectangle1':
            pygame.draw.rect(screen, shape['color'], shape['objRect'])

    # draws the rectangle on the screen
    pygame.draw.rect(screen, BLUE, (rect_pos_x,350,20,10))
   
   # has touched the border
    if rect_pos_x < 0:
        rect_pos_x = 600
        
    # move the rectangle
    rect_pos_x -= 5
    
    # updates the screen
    pygame.display.update()
    
    # stops for 0.02 seconds
    time.sleep(0.02)
        

pygame.quit()