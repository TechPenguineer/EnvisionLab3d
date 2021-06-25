import pygame
run = True
while run:
    background_colour = (56,56,56)
    side_nav_colour = (92, 92, 92)
    canvas = pygame.display.set_mode([500,600])
    canvas.fill(background_colour)
    side_nav = pygame.Surface([50,600])
    side_nav.fill(side_nav_colour)
    canvas.blit(side_nav, [1,1])
    pygame.display.flip()
pygame.quit()

