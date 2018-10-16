import pygame
from classes.maingame import MainGame

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
m_g = MainGame(pygame)

gameDisplay = pygame.display.set_mode((display_width, display_height))
myimage = pygame.image.load('1.jpg').convert()
myimage = pygame.transform.scale(myimage, (35, 35))
clock = pygame.time.Clock()
gameDisplay.blit(myimage, (m_g.img_x, m_g.img_y))


game = True
while game:
    for event in pygame.event.get():
        game = m_g.events_game(event)
        pygame.display.update()

    if m_g.bool_pos:
        m_g.next_position()
        gameDisplay.fill(black)
        gameDisplay.blit(myimage, (m_g.img_x, m_g.img_y))
        pygame.display.update()
        clock.tick(200)

pygame.quit()
