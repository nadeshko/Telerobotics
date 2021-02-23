import pygame

pygame.init()
win = pygame.display.set_mode((200,200))

while True:
    for event in pygame.event.get(): pass
    keyPress = pygame.key.get_pressed()
    if keyPress[pygame.K_a]:
        print('a was pressed!')
    if keyPress[pygame.K_q]:
        print('quitting...')
        break
    pygame.display.update()