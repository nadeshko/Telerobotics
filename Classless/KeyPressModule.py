import pygame
###########################################################################
###                          KEY PRESS MODULE                           ###
###########################################################################

def init():
    """
    Initialize pygame and opens window
    """
    pygame.init()
    screen = pygame.display.set_mode((400, 200))

def getKey(key):
    """
    Detects keyboard input, returns True if keyboard is pressed
    """
    Pressed = False
    for event in pygame.event.get(): pass
    keyPress = pygame.key.get_pressed()
    keyName = getattr(pygame, 'K_{}'.format(key))
    if keyPress[keyName]:
        Pressed = True
    pygame.display.update()
    return Pressed

def main():
    pass

if __name__ == '__main__':
    init()
    while True:
        main()

