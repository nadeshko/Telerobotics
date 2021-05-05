import pygame

###########################################################################
###                          KEY PRESS MODULE                           ###
###########################################################################

class KeyPress():
    def __init__(self):
        """
        Initialize pygame and opens window
        """
        pygame.init()
        screen = pygame.display.set_mode((400, 200))

    def getKey(self, key):
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