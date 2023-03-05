# screen_dim[0] is the x value of the screen
# likewise, screen_dim[1] is the y value of the screen
def moveObj(element, screen_dim):
    screen_left = 0
    screen_top = 0
    screen_right = screen_dim[0]
    screen_bottom = screen_dim[1]

    # checks if the Rect has passed the top or bottom border
    if element['objRect'].top < screen_top or element['objRect'].bottom > screen_bottom:
        element['vel'][1] = element['vel'][1] * (-1)

    # checks if the Rect has passed the left or right border
    if element['objRect'].left < screen_left or element['objRect'].right > screen_right:
        element['vel'][0] = element['vel'][0] * (-1)

    # increases the element's velocity
    element['objRect'].x += element['vel'][0]
    element['objRect'].y += element['vel'][1]
