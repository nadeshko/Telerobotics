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
        win = pygame.display.set_mode((200, 200))

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

'''
def init():
    pygame.init()
    win = pygame.display.set_mode((200,200))

def getKey(key):
    Pressed = False
    for event in pygame.event.get(): pass
    keyPress = pygame.key.get_pressed()
    keyName = getattr(pygame,'K_{}'.format(key))
    if keyPress[keyName]:
        Pressed = True
    pygame.display.update()
    return Pressed

def main():
    pass

if __name__ == '__main__':
    init()
    while True:
        main()'''