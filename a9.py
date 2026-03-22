import pygame
import random


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites with Custom Color Event")


CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  

class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.image.fill(self.color)

sprite1 = MySprite(100, 150, (255, 0, 0))
sprite2 = MySprite(300, 150, (0, 0, 255))


all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)


running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        t
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()