import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Enemies")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 5

# Enemies
enemy_size = 40
num_enemies = 7
enemies = []

for i in range(num_enemies):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, 200)
    enemies.append([x, y])

enemy_speed = 3

# Score
score = 0
font = pygame.font.SysFont(None, 40)

# Collision function
def is_collision(px, py, ex, ey):
    distance = math.sqrt((px - ex)**2 + (py - ey)**2)
    return distance < 40

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Boundaries
    player_x = max(0, min(WIDTH - player_size, player_x))

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Enemies
    for enemy in enemies:
        enemy[1] += enemy_speed

        # Reset enemy if it goes off screen
        if enemy[1] > HEIGHT:
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            enemy[1] = random.randint(0, 200)

        # Check collision
        if is_collision(player_x, player_y, enemy[0], enemy[1]):
            score += 1
            print("Score:", score)

            # Reset enemy after collision
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            enemy[1] = random.randint(0, 200)

        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Display score
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()