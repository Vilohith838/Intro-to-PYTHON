import pygame
import sys


pygame.init()


width = 800
height = 600


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Screen")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


font = pygame.font.SysFont("Arial", 36)


text = font.render("Hello Pygame!", True, BLACK)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, BLUE, (300, 250, 200, 100))

    screen.blit(text, (320, 200))

    pygame.display.update()

pygame.quit()
sys.exit()