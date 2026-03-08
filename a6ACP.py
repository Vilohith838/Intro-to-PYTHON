import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen size
width = 800
height = 600

# Create game window
screen = pygame.display.set_mode((width, height))

# Set window title
pygame.display.set_caption("My First Game Screen")

# Background color (RGB)
background_color = (0, 150, 255)

# Game loop
running = True
while running:
    
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background color
    screen.fill(background_color)

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()